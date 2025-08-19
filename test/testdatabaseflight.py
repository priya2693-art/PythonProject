import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database.models import Base, Flight

# Use in-memory database for testing
TEST_DATABASE_URL = "sqlite:///:memory:"

@pytest.fixture(scope="function")
def session():
    engine = create_engine(TEST_DATABASE_URL)
    Session = sessionmaker(bind=engine)
    Base.metadata.create_all(engine)
    db = Session()

    flight = Flight(flight_id=1, origin="Delhi", destination="Mumbai", price=5000.0, available_seats=100)
    db.add(flight)
    db.commit()

    yield db

    db.close()

def test_flight_info(session):
    flight = session.query(Flight).filter_by(flight_id=1).first()
    info = flight.get_flight_info()
    assert info["origin"] == "Delhi"
    assert info["destination"] == "Mumbai"

def test_book_seats_success(session):
    flight = session.query(Flight).filter_by(flight_id=1).first()
    flight.book_seats(10)
    session.commit()
    assert flight.available_seats == 90

def test_book_seats_failure(session):
    flight = session.query(Flight).filter_by(flight_id=1).first()
    with pytest.raises(ValueError):
        flight.book_seats(1000)

def test_cancel_seats(session):
    flight = session.query(Flight).filter_by(flight_id=1).first()
    flight.cancel_seats(5)
    session.commit()
    assert flight.available_seats == 105


