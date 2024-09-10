from lib.ListingsRepository import *
from lib.Listings import *

def test_get_all_listings(db_connection):
    db_connection.seed("seeds/bnb_db.sql")

    repo = ListingRepository(db_connection)

    all_listings = repo.all()

    assert all_listings == [
        Listing(1, 'Blackpool Tower', 'Really high', 'Blackpool', 25, 1),
        Listing(2, 'London Eye', 'Really round', 'London', 150, 1),
        Listing(3, 'Windsor Castle', 'Really old', 'Windsor', 1150, 2),
        Listing(4, 'SS Great Britain', 'Really wet', 'Bristol', 180, 3)
    ]


def test_check_listing_added(db_connection):
    db_connection.seed("seeds/bnb_db.sql")

    repo = ListingRepository(db_connection)

    listing1 = Listing(None, "test1", "test object", "location", 23, 2)

    repo.add_listing(listing1)

    all_listings = repo.all()

    assert all_listings == [
        Listing(1, 'Blackpool Tower', 'Really high', 'Blackpool', 25, 1),
        Listing(2, 'London Eye', 'Really round', 'London', 150, 1),
        Listing(3, 'Windsor Castle', 'Really old', 'Windsor', 1150, 2),
        Listing(4, 'SS Great Britain', 'Really wet', 'Bristol', 180, 3),
        Listing(5, "test1", "test object", "location", 23, 2)
    ]

    


def test_check_find(db_connection):
    db_connection.seed("seeds/bnb_db.sql")

    repo = ListingRepository(db_connection)

    # listing1 = Listing(1, "test1", "test object", "location", 23)
    # listing2 = Listing(2, "test2", "test objects", "location two", 12)
    # listing3 = Listing(3, "test3", "test objects", "location three", 45)

    # repo.add_listing(listing1)
    # repo.add_listing(listing2)
    # repo.add_listing(listing3)

    found = repo.find(2)

    assert found == Listing(2, 'London Eye', 'Really round', 'London', 150, 1)


# def test_check_add_availability(db_connection):
#     db_connection.seed("seeds/bnb_db.sql")

#     repo = ListingRepository(db_connection)

#     listing1 = Listing(1, "test1", "test object", "location", 23)
#     listing2 = Listing(2, "test2", "test objects", "location two", 12)
#     listing3 = Listing(3, "test3", "test objects", "location three", 45)

#     listing2.add_availability(1234)

#     repo.add_listing(listing1)
#     repo.add_listing(listing2)
#     repo.add_listing(listing3)

#     assert listing2.availability == [1234]


# def test_listings_with_availability(db_connection):
#     db_connection.seed("seeds/bnb_db.sql")

#     repo = ListingRepository(db_connection)

#     listing1 = Listing(1, "test1", "test object", "location", 23)
#     listing2 = Listing(2, "test2", "test objects", "location two", 12)
#     listing3 = Listing(3, "test3", "test objects", "location three", 45)

#     listing2.add_availability(123)
#     listing2.add_availability(456)

#     repo.add_listing(listing1)
#     repo.add_listing(listing2)
#     repo.add_listing(listing3)

#     assert listing2.availability ==  [123, 456]

