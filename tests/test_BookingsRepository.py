from lib.Bookings import *
from lib.BookingsRepository import *
import datetime


def test_find_booking(db_connection):
    db_connection.seed("seeds/bnb_db.sql")

    repo = BookingRepository(db_connection)
    x = datetime.date(2023, 6, 15)
    y = datetime.date(2023, 6, 20)
    
    found = repo.find_booking_by_listing(2)

    assert found == [Booking(2, 2, 3, x, y, 'confirmed')]




def test_find_booking_by_listing_user(db_connection):
    db_connection.seed("seeds/bnb_db.sql")
    repo = BookingRepository(db_connection)

    x = datetime.date(2023, 12, 10)
    y = datetime.date(2023, 12, 10)

    result = repo.find_booking_by_listing_user(2)

    assert result == Listing(3, 'Windsor Castle', 'Really old', 'Windsor', 1150, 2, [Booking(3, 3, 1, x, y, 'requested')])


def test_find_multiple_bookings_by_listing_user(db_connection):
    db_connection.seed("seeds/bnb_db.sql")
    repo = BookingRepository(db_connection)

    listing1_start = datetime.date(2023, 9, 10)
    listing1_end = datetime.date(2023, 9, 12)
    
    listing2_start = datetime.date(2023, 6, 15)
    listing2_end = datetime.date(2023, 6, 20)

    result = repo.find_booking_by_listing_user(1)

    assert result == [Listing(1, 'Blackpool Tower', 'Really high', 'Blackpool', 25, 1, [Booking(1, 1, 2, listing1_start, listing1_end, 'requested')]), Listing(2, 'London Eye', 'Really round', 'London', 150, 1, [Booking(2, 2, 3, listing2_start, listing2_end, 'confirmed')])]

def test_booking_not_available(db_connection):
    db_connection.seed("seeds/bnb_db.sql")
    repo = BookingRepository(db_connection)

    x = datetime.date(2023, 6, 16)
    y = datetime.date(2023, 6, 16)
    result = repo.is_listing_available(2, x, y)
    assert result == False

def test_booking_is_available(db_connection):
    db_connection.seed("seeds/bnb_db.sql")
    repo = BookingRepository(db_connection)

    x = datetime.date(2023, 6, 16)
    y = datetime.date(2023, 6, 16)
    result = repo.is_listing_available(1, x, y)
    assert result == True

def test_create_booking(db_connection):
    db_connection.seed("seeds/bnb_db.sql")
    repo = BookingRepository(db_connection)

    x = datetime.date(2023, 12, 16)
    y = datetime.date(2023, 12, 16)
    
    create_result = repo.create_booking(4, 1, x, y)
    result = repo.find_booking_by_listing(4)
    assert result == [Booking(4, 4, 1, x, y, 'requested')]
    assert create_result == "Booking submitted successfully"