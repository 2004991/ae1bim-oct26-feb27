
from configuracion import Session
from crear_base_entidades import HistoriaClinica

# Crear una sesion para consultar SQLite
session = Session()

try:
    # Buscar historias clinicas con diagnostico Gastritis
    resultados = (
        session.query(HistoriaClinica)
        .filter(HistoriaClinica.diagnostico == "Gastritis")
        .all()
    )

    print("\nCONSULTA FILTER - DIAGNOSTICO GASTRITIS")
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
