import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database.models import Base, Hotel


TEST_DB_URL = "sqlite:///:memory:"

@pytest.fixture(scope="function")
def session():
    engine = create_engine(TEST_DB_URL)
    Session = sessionmaker(bind=engine)
    Base.metadata.create_all(engine)
    db = Session()

    # Seed test hotel
    hotel = Hotel(hotel_id=1, name="Taj Palace", location="Delhi", price_per_night=8000.0, available_room=50)
    db.add(hotel)
    db.commit()

    yield db
    db.close()

def test_get_hotel_info(session):
    hotel = session.query(Hotel).filter_by(hotel_id=1).first()
    info = hotel.get_hotel_info()
    assert info["name"] == "Taj Palace"
    assert info["location"] == "Delhi"
    assert info["available_room"] == 50

def test_book_rooms_success(session):
    hotel = session.query(Hotel).filter_by(hotel_id=1).first()
    result = hotel.book_rooms(5)
    session.commit()
    assert result is True
    assert hotel.available_room == 45

def test_book_rooms_failure(session):
    hotel = session.query(Hotel).filter_by(hotel_id=1).first()
    with pytest.raises(ValueError):
        hotel.book_rooms(100)

def test_cancel_rooms(session):
    hotel = session.query(Hotel).filter_by(hotel_id=1).first()
    hotel.cancel_rooms(3)
    session.commit()
    assert hotel.available_room == 53

def test_price_calculation(session):
    hotel = session.query(Hotel).filter_by(hotel_id=1).first()
    total_price = hotel.get_price_for_rooms(2, 3)  # 2 rooms, 3 nights
    assert total_price == 48000.0
