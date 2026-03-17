from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "postgresql://vallehealth_user:s1TkCtRlEeM8IkG6Zuv6O3qUIZnlcpzJ@dpg-d6sc99pj16oc73em07h0-a.oregon-postgres.render.com/vallehealth"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
