from lib.Bookings import *
from lib.BookingsRepository import *
import datetime


def test_find_booking(db_connection):
    db_connection.seed("seeds/bnb_db.sql")

    repo = BookingRepository(db_connection)
    x = datetime.date(2023, 12, 10)
    y = datetime.date(2023, 12, 10)
    
    found = repo.find_booking_by_listing(3)

    assert found == [Booking(5, 3, 1, 'Catherine', x, y, 'requested','Windsor Castle', 1150)]

def test_find_booking_requester_id(db_connection):
    db_connection.seed("seeds/bnb_db.sql")

    repo = BookingRepository(db_connection)
    x = datetime.date(2023, 12, 10)
    y = datetime.date(2023, 12, 10)
    
    found = repo.find_booking_by_requester_id(1)

    assert found == [Booking(5, 3, 1, 'Catherine', x, y, 'requested','Windsor Castle', 1150)]



def test_find_booking_by_listing_user(db_connection):
    db_connection.seed("seeds/bnb_db.sql")
    repo = BookingRepository(db_connection)

    x = datetime.date(2023, 12, 10)
    y = datetime.date(2023, 12, 10)

    result = repo.find_booking_by_listing_user(2)

    assert result == [Listing(3, 'Windsor Castle', 'Really old', 'Windsor', 1150, 2, [Booking(5, 3, 1, 'Catherine', x, y, 'requested','Windsor Castle', 1150)])]


def test_find_multiple_bookings_by_multiple_listings_user(db_connection):
    db_connection.seed("seeds/bnb_db.sql")
    repo = BookingRepository(db_connection)

    listing1_start = datetime.date(2023, 9, 10)
    listing1_end = datetime.date(2023, 9, 12)
    
    listing2_start = datetime.date(2023, 10, 10)
    listing2_end = datetime.date(2023, 10, 12)

    listing3_start = datetime.date(2023, 6, 15)
    listing3_end = datetime.date(2023, 6, 20)

    listing4_start = datetime.date(2023, 12, 15)
    listing4_end = datetime.date(2023, 12, 20)

    result = repo.find_booking_by_listing_user(1)

    assert result == [Listing(1, 'Blackpool Tower', 'Really high', 'Blackpool', 25, 1, [Booking(1, 1, 2, 'Sarah', listing1_start, listing1_end, 'requested', 'Blackpool Tower', 25), Booking(2, 1, 3,'Andy', listing2_start, listing2_end, 'requested', 'Blackpool Tower', 25)]), Listing(2, 'London Eye', 'Really round', 'London', 150, 1, [Booking(3, 2, 3, 'Andy', listing3_start, listing3_end, 'confirmed', 'London Eye', 150), Booking(4, 2, 3, 'Andy', listing4_start, listing4_end, 'confirmed', 'London Eye', 150)])]


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
    
    create_result = repo.create_booking(4, 1, 'Catherine', x, y, 'SS Great Britain', 180)
    result = repo.find_booking_by_listing(4)
    assert result == [Booking(6, 4, 1,'Catherine', x, y, 'requested', 'SS Great Britain', 180)]
    assert create_result == "Booking submitted successfully"

def test_change_status_from_requested_to_confirmed(db_connection):
    db_connection.seed("seeds/bnb_db.sql")
    repo = BookingRepository(db_connection)
    repo.change_status_from_requested_to_confirmed(1, 2)
    result = repo.find_booking_by_requester_id(2)
    x = datetime.date(2023, 9, 10)
    y = datetime.date(2023, 9, 12)
    assert result == [Booking(1, 1, 2, 'Sarah', x, y, 'confirmed', 'Blackpool Tower', 25)]

def test_change_status_from_requested_to_denied(db_connection):
    db_connection.seed("seeds/bnb_db.sql")
    repo = BookingRepository(db_connection)
    repo.change_status_from_requested_to_denied(1, 2)
    result = repo.find_booking_by_requester_id(2)
    x = datetime.date(2023, 9, 10)
    y = datetime.date(2023, 9, 12)
    assert result == [Booking(1, 1, 2, 'Sarah', x, y, 'denied', 'Blackpool Tower', 25)]