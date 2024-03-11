from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker, declarative_base
import os

db_user = os.getenv('DB_USER', 'laad')
db_password = os.getenv('DB_PASS', 'ladd')
db_host = os.getenv('DB_HOST', 'localhost')
db_port = os.getenv('DB_PORT', 5434)
db_name = os.getenv('DB_NAME', 'pda')

connect_args={
            "keepalives": 1,
            "keepalives_idle": 30,
            "keepalives_interval": 10,
            "keepalives_count": 5,
        }
connect_string=f"postgresql+psycopg2://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"

engine = create_engine(connect_string,
                       pool_size=10,
                       max_overflow=2,
                       pool_recycle=300,
                       pool_pre_ping=True,
                       connect_args=connect_args)

db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()

def init_db():
    # import all modules here that might define models so that
    # they will be registered properly on the metadata.  Otherwise
    # you will have to import them first before calling init_db()
    from src.auditoria.modulos.auditoria.infraestructura.dto import Propiedad
    Base.metadata.create_all(bind=engine)