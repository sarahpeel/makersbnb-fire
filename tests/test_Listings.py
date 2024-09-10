# from lib.Listings import Listing

# def test_listing_creates_correct_variables():
#     listing1 = Listing(1, "test1", "fake description 1", "location1", 5)
#     assert listing1.name == "test1"
#     assert listing1.id == 1
#     assert listing1.description == "fake description 1"
#     assert listing1.price == 5

# def test_add_availability():
#     listing1 = Listing(1, "test1", "fake description 1", "location1", 5)
#     listing1.add_availability(1234)
#     assert listing1.availability == [1234]

# def test_repr_works_with_avaialability():
#     listing2 = Listing(2, "test1", "fake description 1", "location1", 5)
#     listing2.add_availability(5678)
#     assert listing2.__repr__() == 'Listing(2, test1, fake description 1, location1, 5, False, [5678])'

# def test_repr_works_with_avaialability_no_dupe_lists():
#     listing1 = Listing(1, "test1", "fake description 1", "location1", 5)
#     listing1.add_availability(5678)
#     assert listing1.__repr__() == 'Listing(1, test1, fake description 1, location1, 5, False, [5678])'
