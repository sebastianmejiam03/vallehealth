import pandas as pd
from sqlalchemy import create_engine, text

DB_URL = "postgresql://sebastianmejia@localhost/vallehealth"
engine = create_engine(DB_URL)

print("Leyendo archivo...")
df = pd.read_excel('/Users/sebastianmejia/Downloads/Datos_2023_210.xlsx')

print(f"Total registros: {len(df)}")

# Filtrar Valle del Cauca
valle = df[df['Departamento_ocurrencia'] == 'VALLE'].copy()
print(f"Registros Valle del Cauca: {len(valle)}")

# Insertar municipios únicos
municipios = valle['Municipio_ocurrencia'].dropna().unique()
with engine.connect() as conn:
    for mun in municipios:
        conn.execute(text("""
            INSERT INTO municipios (nombre, codigo_dane, latitud, longitud, poblacion)
            VALUES (:nombre, '76000', 0, 0, 0)
            ON CONFLICT DO NOTHING
        """), {"nombre": str(mun)})
    conn.commit()
print(f"Municipios insertados: {len(municipios)}")

# Insertar enfermedad Dengue
with engine.connect() as conn:
    conn.execute(text("""
        INSERT INTO enfermedades (nombre, codigo_sivigila, descripcion, umbral_alerta, categoria)
        VALUES ('Dengue', 'DEN210', 'Enfermedad viral transmitida por mosquito Aedes aegypti', 100, 'infecciosa')
        ON CONFLICT DO NOTHING
    """))
    conn.commit()

# Obtener IDs
with engine.connect() as conn:
    mun_ids = {row[0]: row[1] for row in conn.execute(text("SELECT nombre, id FROM municipios"))}
    enf_id = conn.execute(text("SELECT id FROM enfermedades WHERE nombre='Dengue'")).scalar()

# Insertar casos
print("Insertando casos...")
count = 0
with engine.connect() as conn:
    for _, row in valle.iterrows():
        mun_nombre = str(row.get('Municipio_ocurrencia', ''))
        mun_id = mun_ids.get(mun_nombre)
        if not mun_id:
            continue
        try:
            conn.execute(text("""
                INSERT INTO casos_enfermedades 
                (municipio_id, enfermedad_id, anio, semana_epi, num_casos, sexo, grupo_edad, fecha_registro)
                VALUES (:mun_id, :enf_id, :anio, :semana, 1, :sexo, :edad, CURRENT_DATE)
            """), {
                "mun_id": mun_id,
                "enf_id": enf_id,
                "anio": int(row.get('ANO', 2023)),
                "semana": int(row.get('SEMANA', 1)),
                "sexo": str(row.get('SEXO', 'M'))[:1],
                "edad": str(row.get('EDAD', ''))[:20]
            })
            count += 1
        except:
            continue
    conn.commit()

print(f"✅ Casos insertados: {count}")
