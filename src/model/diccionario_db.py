from src.model.i_diccionario import IDiccionario
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.model.db import SupervisorDB, ActividadDB, AnexosDB

class Consulta(IDiccionario):
    """
    Representa la verificacion de un supervisor en la base de datos.
    """
    
    def __init__(self):
        """
        Inicializa una instancia de la clase Consulta, creando la conexión a la base de datos.
        """
        url_conexion = "postgresql://jeron:@localhost:5432/Bitacora"
        engine = create_engine(url_conexion, echo = True)
        session = sessionmaker(bind=engine)
        self.database_session = session()
    
    
    def verificar_supervisor(self, email: str, contraseña: str) -> bool:
        supervisor = self.database_session.query(SupervisorDB).filter_by(email=email, contraseña=contraseña).first()
        return supervisor is not None

    def registrar_supervisor(self, nombre: str, email: str, contraseña: str) -> bool:
        existente = self.database_session.query(SupervisorDB).filter_by(email=email).first()
        if existente:
            return False  # Ya existe
        nuevo_supervisor = SupervisorDB(nombre=nombre, email=email, contraseña=contraseña)
        self.database_session.add(nuevo_supervisor)
        self.database_session.commit()
        return True