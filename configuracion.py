
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

# Nombre y ubicación de la base de datos SQLite
DATABASE_URL = "sqlite:///veterinarias.db"

# Crear el motor de conexión
engine = create_engine(DATABASE_URL, echo=True)

# Crear las sesiones para trabajar con la base de datos
Session = sessionmaker(bind=engine)

# Clase base para definir las entidades
Base = declarative_base()

from sqlalchemy import event

# Activar la comprobacion de claves foraneas en SQLite
@event.listens_for(engine, "connect")
def activar_claves_foraneas(dbapi_connection, connection_record):
    cursor = dbapi_connection.cursor()
    cursor.execute("PRAGMA foreign_keys=ON")
    cursor.close()

