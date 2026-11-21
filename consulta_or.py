
from sqlalchemy import or_
from configuracion import Session
from crear_base_entidades import HistoriaClinica

# Crear una sesion para consultar SQLite
session = Session()

try:
    # Buscar historias con Gastritis o Dermatitis
    resultados = (
        session.query(HistoriaClinica)
        .filter(
            or_(
                HistoriaClinica.diagnostico == "Gastritis",
                HistoriaClinica.diagnostico == "Dermatitis"
            )
        )
        .order_by(HistoriaClinica.id)
        .all()
    )

    print("\nCONSULTA OR - GASTRITIS O DERMATITIS")
    print("-" * 55)

    if resultados:
        for historia in resultados:
            print(f"ID: {historia.id}")
            print(f"Mascota: {historia.nombre_mascota}")
            print(f"Fecha: {historia.fecha_atencion}")
            print(f"Diagnostico: {historia.diagnostico}")
            print(f"Tratamiento: {historia.tratamiento}")
            print("-" * 55)
    else:
        print("No se encontraron historias clinicas.")

    print(f"TOTAL DE RESULTADOS: {len(resultados)}")

except Exception as error:
    print("Error al consultar:", error)

finally:
    session.close()
