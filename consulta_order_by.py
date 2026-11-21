
from configuracion import Session
from crear_base_entidades import HistoriaClinica

# Crear una sesion para consultar SQLite
session = Session()

try:
    # Consultar historias ordenadas por fecha descendente
    resultados = (
        session.query(HistoriaClinica)
        .order_by(HistoriaClinica.fecha_atencion.desc())
        .all()
    )

    print("\nCONSULTA ORDER_BY - HISTORIAS POR FECHA")
    print("-" * 60)

    for historia in resultados:
        print(f"ID: {historia.id}")
        print(f"Mascota: {historia.nombre_mascota}")
        print(f"Fecha: {historia.fecha_atencion}")
        print(f"Diagnostico: {historia.diagnostico}")
        print("-" * 60)

    print(f"TOTAL DE HISTORIAS: {len(resultados)}")

except Exception as error:
    print("Error al consultar:", error)

finally:
    session.close()
