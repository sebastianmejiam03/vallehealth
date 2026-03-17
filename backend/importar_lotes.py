import pandas as pd
from sqlalchemy import create_engine, text

DB_URL = "postgresql://vallehealth_user:s1TkCtRlEeM8IkG6Zuv6O3qUIZnlcpzJ@dpg-d6sc99pj16oc73em07h0-a.oregon-postgres.render.com/vallehealth"
engine = create_engine(DB_URL, connect_args={"connect_timeout": 60})

print("Leyendo archivo...")
df = pd.read_excel('/Users/sebastianmejia/Downloads/Datos_2023_210.xlsx')
valle = df[df['Departamento_ocurrencia'] == 'VALLE'].copy()

with engine.connect() as conn:
    mun_ids = {row[0]: row[1] for row in conn.execute(text("SELECT nombre, id FROM municipios"))}
    enf_id = conn.execute(text("SELECT id FROM enfermedades WHERE nombre='Dengue'")).scalar()

records = []
for _, row in valle.iterrows():
    mun_id = mun_ids.get(str(row.get('Municipio_ocurrencia', '')))
    if not mun_id:
        continue
    records.append({
        "mun_id": mun_id, "enf_id": enf_id,
        "anio": int(row.get('ANO', 2023)),
        "semana": int(row.get('SEMANA', 1)),
        "sexo": str(row.get('SEXO', 'M'))[:1],
        "edad": str(row.get('EDAD', ''))[:20]
    })

LOTE = 500
total = 0
for i in range(0, len(records), LOTE):
    lote = records[i:i+LOTE]
    with engine.connect() as conn:
        conn.execute(text("""
            INSERT INTO casos_enfermedades
            (municipio_id, enfermedad_id, anio, semana_epi, num_casos, sexo, grupo_edad, fecha_registro)
            VALUES (:mun_id, :enf_id, :anio, :semana, 1, :sexo, :edad, CURRENT_DATE)
        """), lote)
        conn.commit()
    total += len(lote)
    print(f"Insertados: {total}/{len(records)}")

print(f"✅ Total insertados: {total}")
