from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .models import Base

engine = create_engine('sqlite:///flights.db', echo=True)
SessionLocal = sessionmaker(bind=engine)

def init_db():
    Base.metadata.create_all(bind=engine)


def save_lead_to_db(lead_obj):
    session = SessionLocal()
    try:
        session.add(lead_obj)
        session.commit()
        print("Lead saved successfully.")
    except Exception as e:
        session.rollback()
        print(f"Error saving lead: {e}")
    finally:
        session.close()
