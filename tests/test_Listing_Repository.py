from lib.ListingsRepository import *
from lib.Listings import *

def test_get_all_listings(db_connection):
    db_connection.seed("seeds/bnb_db.sql")

    repo = ListingRepository(db_connection)

    all_listings = repo.all()

    assert all_listings == []


def test_check_listing_added(db_connection):
    db_connection.seed("seeds/bnb_db.sql")

    repo = ListingRepository(db_connection)

    listing1 = Listing(1, "test1", "test object", "location", 23)

    repo.add_listing(listing1)

    all_listings = repo.all()

    assert all_listings == [
        Listing(1, "test1", "test object", "location", 23, False)
    ]

    assert all_listings[0].availability  == []


def test_check_find(db_connection):
    db_connection.seed("seeds/bnb_db.sql")

    repo = ListingRepository(db_connection)

    listing1 = Listing(1, "test1", "test object", "location", 23)
    listing2 = Listing(2, "test2", "test objects", "location two", 12)
    listing3 = Listing(3, "test3", "test objects", "location three", 45)

    repo.add_listing(listing1)
    repo.add_listing(listing2)
    repo.add_listing(listing3)

    found = repo.find(2)

    assert found == Listing(2, "test2", "test objects", "location two", 12)


def test_check_add_availability(db_connection):
    db_connection.seed("seeds/bnb_db.sql")

    repo = ListingRepository(db_connection)

    listing1 = Listing(1, "test1", "test object", "location", 23)
    listing2 = Listing(2, "test2", "test objects", "location two", 12)
    listing3 = Listing(3, "test3", "test objects", "location three", 45)

    listing2.add_availability(1234)

    repo.add_listing(listing1)
    repo.add_listing(listing2)
    repo.add_listing(listing3)

    assert listing2.availability == [1234]


def test_listings_with_availability(db_connection):
    db_connection.seed("seeds/bnb_db.sql")

    repo = ListingRepository(db_connection)

    listing1 = Listing(1, "test1", "test object", "location", 23)
    listing2 = Listing(2, "test2", "test objects", "location two", 12)
    listing3 = Listing(3, "test3", "test objects", "location three", 45)

    listing2.add_availability(123)
    listing2.add_availability(456)

    repo.add_listing(listing1)
    repo.add_listing(listing2)
    repo.add_listing(listing3)

    assert listing2.availability ==  [123, 456]

