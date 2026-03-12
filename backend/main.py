from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from database import get_db, engine
import models

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="ValleHealth API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# ── MUNICIPIOS ──────────────────────────────
@app.get("/municipios")
def get_municipios(db: Session = Depends(get_db)):
    return db.query(models.Municipio).all()

@app.get("/municipios/{id}")
def get_municipio(id: int, db: Session = Depends(get_db)):
    m = db.query(models.Municipio).filter(models.Municipio.id == id).first()
    if not m:
        raise HTTPException(status_code=404, detail="Municipio no encontrado")
    return m

# ── ENFERMEDADES ─────────────────────────────
@app.get("/enfermedades")
def get_enfermedades(db: Session = Depends(get_db)):
    return db.query(models.Enfermedad).all()

@app.get("/enfermedades/{id}")
def get_enfermedad(id: int, db: Session = Depends(get_db)):
    e = db.query(models.Enfermedad).filter(models.Enfermedad.id == id).first()
    if not e:
        raise HTTPException(status_code=404, detail="Enfermedad no encontrada")
    return e

# ── CASOS ────────────────────────────────────
@app.get("/casos")
def get_casos(
    municipio_id: int = None,
    enfermedad_id: int = None,
    anio: int = None,
    db: Session = Depends(get_db)
):
    query = db.query(models.CasoEnfermedad)
    if municipio_id:
        query = query.filter(models.CasoEnfermedad.municipio_id == municipio_id)
    if enfermedad_id:
        query = query.filter(models.CasoEnfermedad.enfermedad_id == enfermedad_id)
    if anio:
        query = query.filter(models.CasoEnfermedad.anio == anio)
    return query.all()

# ── ALERTAS ──────────────────────────────────
@app.get("/alertas")
def get_alertas(db: Session = Depends(get_db)):
    return db.query(models.Alerta).filter(models.Alerta.activa == True).all()

# ── USUARIOS ─────────────────────────────────
@app.get("/usuarios")
def get_usuarios(db: Session = Depends(get_db)):
    return db.query(models.Usuario).all()

@app.post("/login")
def login(email: str, password: str, db: Session = Depends(get_db)):
    user = db.query(models.Usuario).filter(models.Usuario.email == email).first()
    if not user:
        raise HTTPException(status_code=401, detail="Credenciales incorrectas")
    return {"mensaje": "Login exitoso", "rol": user.rol}
    