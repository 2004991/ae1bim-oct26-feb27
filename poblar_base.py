

from datetime import date

from configuracion import Session
from crear_base_entidades import (
    Clinica,
    Consultorio,
    Veterinario,
    HistoriaClinica
)


# Crear la sesion de trabajo
session = Session()

try:
    
    # Crear las clinicas si todavia no existen
    datos_clinicas = [
        ("Huellitas Felices", "Av. 9 de Octubre, El Coca",
         "Carlos Andrade"),
        ("Mundo Animal", "Av. Amazonas, Quito",
         "Maria Lopez"),
        ("Patitas Sanas", "Av. Cevallos, Ambato",
         "Jose Ramirez")
    ]

    clinicas = []

    for nombre, direccion, responsable in datos_clinicas:

        clinica = session.query(Clinica).filter_by(
            nombre=nombre
        ).first()

        if clinica is None:
            clinica = Clinica(
                nombre=nombre,
                direccion=direccion,
                veterinario_responsable=responsable
            )

            session.add(clinica)
            session.flush()

            print(f"Clinica creada: {nombre}")
        else:
            print(f"Clinica existente: {nombre}")

        clinicas.append(clinica)

    # Recuperar las tres clinicas para asociar consultorios
    clinica1, clinica2, clinica3 = clinicas

    print("Las tres clinicas estan disponibles.")

    

    # Datos de los consultorios
    datos_consultorios = [
        ("Consultorio 1", "Medicina general", clinica1),
        ("Consultorio 2", "Cirugia", clinica1),
        ("Consultorio 3", "Dermatologia", clinica2),
        ("Consultorio 4", "Medicina general", clinica2),
        ("Consultorio 5", "Odontologia", clinica3),
        ("Consultorio 6", "Cirugia", clinica3)
    ]

    # Registrar solamente consultorios que no existan
    for nombre, especialidad, clinica in datos_consultorios:

        existente = session.query(Consultorio).filter_by(
            nombre=nombre,
            clinica_id=clinica.id
        ).first()

        if existente is None:
            nuevo_consultorio = Consultorio(
                nombre=nombre,
                especialidad=especialidad,
                clinica_id=clinica.id
            )

            session.add(nuevo_consultorio)
            print(f"Registrando: {nombre} - {clinica.nombre}")
        else:
            print(f"Ya existe: {nombre} - {clinica.nombre}")

    # Guardar los datos definitivamente
    session.commit()

    # Registrar los veterinarios
    datos_veterinarios = [
        ("Carlos", "Andrade", "carlos@ejemplo.com", "VET-001", "Consultorio 1"),
        ("Ana", "Torres", "ana@ejemplo.com", "VET-002", "Consultorio 2"),
        ("Maria", "Lopez", "maria@ejemplo.com", "VET-003", "Consultorio 3"),
        ("Pedro", "Sanchez", "pedro@ejemplo.com", "VET-004", "Consultorio 4"),
        ("Jose", "Ramirez", "jose@ejemplo.com", "VET-005", "Consultorio 5"),
        ("Laura", "Mendoza", "laura@ejemplo.com", "VET-006", "Consultorio 6")
    ]

    for nombres, apellidos, correo, licencia, nombre_consultorio in datos_veterinarios:

        # Buscar el consultorio correspondiente
        consultorio = session.query(Consultorio).filter_by(
            nombre=nombre_consultorio
        ).first()

        if consultorio is None:
            raise ValueError(
                f"No existe el consultorio: {nombre_consultorio}"
            )

        # Evitar registrar licencias duplicadas
        existente = session.query(Veterinario).filter_by(
            licencia_profesional=licencia
        ).first()

        if existente is None:
            veterinario = Veterinario(
                nombres=nombres,
                apellidos=apellidos,
                correo=correo,
                licencia_profesional=licencia,
                consultorio_id=consultorio.id
            )

            session.add(veterinario)
            print(f"Registrando veterinario: {nombres} {apellidos}")
        else:
            print(f"Veterinario existente: {nombres} {apellidos}")

    # Guardar los veterinarios
    session.commit()




    # Registrar las historias clinicas
    datos_historias = [
        ("2026-10-01", "Max", "Gastritis",
         "Dieta blanda y medicamentos", "VET-001"),

        ("2026-10-02", "Luna", "Infeccion respiratoria",
         "Antibioticos prescritos", "VET-001"),

        ("2026-10-03", "Rocky", "Fractura",
         "Inmovilizacion y seguimiento", "VET-002"),

        ("2026-10-04", "Toby", "Herida superficial",
         "Limpieza y curaciones", "VET-002"),

        ("2026-10-05", "Bella", "Dermatitis",
         "Tratamiento dermatologico", "VET-003"),

        ("2026-10-06", "Nala", "Alergia cutanea",
         "Tratamiento antialergico", "VET-003"),

        ("2026-10-07", "Milo", "Fiebre",
         "Control y medicamentos", "VET-004"),

        ("2026-10-08", "Coco", "Parasitosis",
         "Desparasitacion", "VET-004"),

        ("2026-10-09", "Kira", "Gingivitis",
         "Limpieza dental", "VET-005"),

        ("2026-10-10", "Simba", "Sarro dental",
         "Profilaxis dental", "VET-005"),

        ("2026-10-11", "Zeus", "Lesion muscular",
         "Reposo y tratamiento", "VET-006"),

        ("2026-10-12", "Lola", "Herida profunda",
         "Sutura y seguimiento", "VET-006")
    ]

    for fecha, mascota, diagnostico, tratamiento, licencia in datos_historias:

        # Buscar al veterinario responsable
        veterinario = session.query(Veterinario).filter_by(
            licencia_profesional=licencia
        ).first()

        if veterinario is None:
            raise ValueError(
                f"No existe el veterinario con licencia {licencia}"
            )

        # Evitar duplicar historias al ejecutar nuevamente
        fecha_atencion = date.fromisoformat(fecha)

        existente = session.query(HistoriaClinica).filter_by(
            fecha_atencion=fecha_atencion,
            nombre_mascota=mascota,
            veterinario_id=veterinario.id
        ).first()

        if existente is None:
            historia = HistoriaClinica(
                fecha_atencion=fecha_atencion,
                nombre_mascota=mascota,
                diagnostico=diagnostico,
                tratamiento=tratamiento,
                veterinario_id=veterinario.id
            )

            session.add(historia)
            print(f"Registrando historia clinica: {mascota}")
        else:
            print(f"Historia clinica existente: {mascota}")

    # Guardar las historias clinicas
    session.commit()

    # Verificar el total
    total_historias = session.query(HistoriaClinica).count()
    print("Historias clinicas registradas:", total_historias)


    # Verificar el total
    total_veterinarios = session.query(Veterinario).count()
    print("Veterinarios registrados:", total_veterinarios)

    # Comprobar el numero de consultorios
    total = session.query(Consultorio).count()

    print("--------------------------------")
    print("Consultorios registrados:", total)
    print("Proceso finalizado correctamente.")

except Exception as error:
    session.rollback()
    print("Ocurrio un error:", error)

finally:
    session.close()
