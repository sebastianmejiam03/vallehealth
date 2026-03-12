from sqlalchemy import Column, Integer, String, Date, Boolean, Numeric, Text, Enum
from database import Base
import enum

class RolEnum(str, enum.Enum):
    ciudadano = "ciudadano"
    admin = "admin"

class NivelEnum(str, enum.Enum):
    bajo = "bajo"
    medio = "medio"
    alto = "alto"

class Municipio(Base):
    __tablename__ = "municipios"
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100))
    codigo_dane = Column(String(10))
    latitud = Column(Numeric(9, 6))
    longitud = Column(Numeric(9, 6))
    poblacion = Column(Integer)

class Enfermedad(Base):
    __tablename__ = "enfermedades"
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100))
    codigo_sivigila = Column(String(10))
    descripcion = Column(Text)
    umbral_alerta = Column(Integer)
    categoria = Column(String(50))

class CasoEnfermedad(Base):
    __tablename__ = "casos_enfermedades"
    id = Column(Integer, primary_key=True, index=True)
    municipio_id = Column(Integer)
    enfermedad_id = Column(Integer)
    anio = Column(Integer)
    semana_epi = Column(Integer)
    num_casos = Column(Integer)
    sexo = Column(String(1))
    grupo_edad = Column(String(20))
    fecha_registro = Column(Date)

class Usuario(Base):
    __tablename__ = "usuarios"
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100))
    email = Column(String(100), unique=True)
    password_hash = Column(String(255))
    rol = Column(Enum(RolEnum))
    activo = Column(Boolean, default=True)

class Alerta(Base):
    __tablename__ = "alertas"
    id = Column(Integer, primary_key=True, index=True)
    municipio_id = Column(Integer)
    enfermedad_id = Column(Integer)
    nivel = Column(Enum(NivelEnum))
    fecha_alerta = Column(Date)
    activa = Column(Boolean, default=True)
    