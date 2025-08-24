from fastapi import APIRouter
from app.db.session import SessionLocal

router = APIRouter(prefix="/org", tags=["org"])

@router.post("/seed")
def seed():
    db = SessionLocal()
    try:
        db.execute("CREATE TABLE IF NOT EXISTS units (id SERIAL PRIMARY KEY, name TEXT UNIQUE NOT NULL);")
        db.execute("CREATE TABLE IF NOT EXISTS departments (id SERIAL PRIMARY KEY, name TEXT UNIQUE NOT NULL);")
        db.execute("CREATE TABLE IF NOT EXISTS machines (id SERIAL PRIMARY KEY, name TEXT UNIQUE NOT NULL);")
        db.execute("CREATE TABLE IF NOT EXISTS shifts (id SERIAL PRIMARY KEY, name TEXT UNIQUE NOT NULL);")
        db.execute("INSERT INTO units (name) VALUES ('Mill A') ON CONFLICT DO NOTHING;")
        db.execute("INSERT INTO departments (name) VALUES ('Weaving') ON CONFLICT DO NOTHING;")
        db.execute("INSERT INTO machines (name) VALUES ('Loom-01') ON CONFLICT DO NOTHING;")
        db.execute("INSERT INTO shifts (name) VALUES ('Shift-1') ON CONFLICT DO NOTHING;")
        db.commit()
        return {"ok": True}
    finally:
        db.close()
