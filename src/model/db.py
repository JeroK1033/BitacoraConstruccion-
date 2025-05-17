from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship


Base = declarative_base()

class SupervisorDB(Base):  
    __tablename__ = 'supervisor'
    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(30), nullable=False)
    email = Column(String(50), unique=True, nullable=False)
    contraseña = Column(String(20), nullable=False)
    
class ActividadDB(Base):  
    __tablename__ = 'actividades'
    id = Column(Integer, primary_key=True, autoincrement=True)
    descripcion = Column(String(200), nullable=False)
    fecha = Column(String(10), nullable=False)  # Formato YYYY-MM-DD
    hora = Column(String(5), nullable=False)  # Formato HH:MM
    condiciones_climaticas = Column(String(100), nullable=False)
    supervisor = relationship("SupervisorDB", backref="actividades")
    
class AnexosDB(Base):  
    __tablename__ = 'anexos'
    id = Column(Integer, primary_key=True, autoincrement=True)
    ruta_archivo = Column(String(255), nullable=False)
    tipo_archivo = Column(String(50), nullable=False) 
    actividad = relationship("ActividadDB", backref="anexos")