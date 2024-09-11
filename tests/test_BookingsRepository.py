from lib.Bookings import *
from lib.BookingsRepository import *
import datetime


def test_find_booking(db_connection):
    db_connection.seed("seeds/bnb_db.sql")

    repo = BookingRepository(db_connection)
    x = datetime.date(2023, 6, 15)
    y = datetime.date(2023, 6, 20)
    
    found = repo.find_booking(2)

    assert found == [Booking(2, 2, 3, x, y, 'confirmed')]