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
    
    
    def __obtener_supervisores(self):
        """
        Obtiene los supervisores que hay registrados en la base de datos 
        
        returns:
            list[SupervisorDB]: Lista de supervisores registrados en la base de datos.
        """
        supervisor = self.database_session.query(SupervisorDB).all()
        
        return supervisor
    
    
    def verificar_supervisor(self, email: str, contraseña: str) -> bool:
        """
        Verifica si el supervisor existe en la base de datos.
        
        Atributes:
            email (str): El correo electrónico del supervisor.
            contraseña (str): La contraseña del supervisor.
        
        Returns:
            bool: True si el supervisor existe, False en caso contrario.
        """
        supervisor = self.database_session.query(SupervisorDB).filter_by(email=email, contraseña=contraseña).first()
        if supervisor:
            return True
        return False
    
    
    def registrar_supervisor(self, nombre: str, email: str, contraseña: str) -> bool:

        """
        Registra un nuevo supervisor en la base de datos, pero primero verifica si el supervisor ya existe.

        Returns:
            Bool: True si el supervisor fue registrado correctamente, False si ya existe.
        """
        existente = self.database_session.query(SupervisorDB).filter_by(email=email).first()
        if existente:
            return False

        nuevo_supervisor = SupervisorDB(nombre=nombre, email=email, contraseña=contraseña)
        self.database_session.add(nuevo_supervisor)
        self.database_session.commit()
        return True
