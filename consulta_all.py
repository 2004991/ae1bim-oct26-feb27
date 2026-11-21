
from sqlalchemy import func
from configuracion import Session
from crear_base_entidades import (
    Clinica,
    Consultorio,
    Veterinario,
    HistoriaClinica
)

# Crear la sesion
session = Session()

try:
    # Consultar todas las clinicas y contar sus historias
    resultados = (
        session.query(
            Clinica.nombre,
            func.count(HistoriaClinica.id).label("total_historias")
        )
        .outerjoin(Consultorio, Clinica.id == Consultorio.clinica_id)
        .outerjoin(Veterinario, Consultorio.id == Veterinario.consultorio_id)
        .outerjoin(HistoriaClinica, Veterinario.id == HistoriaClinica.veterinario_id)
        .group_by(Clinica.id, Clinica.nombre)
        .order_by(Clinica.id)
        .all()
    )

    print("\nCONSULTA ALL - HISTORIAS CLINICAS POR CLINICA")
    print("-" * 55)

    total_general = 0

    for nombre, cantidad in resultados:
        print(f"Clinica: {nombre}")
        print(f"Numero de historias clinicas: {cantidad}")
        print("-" * 55)
        total_general += cantidad

    print(f"TOTAL GENERAL DE HISTORIAS: {total_general}")

except Exception as error:
    print("Error al consultar:", error)

finally:
    session.close()
