from lib.listing import Listing 

"""
Listing constructs id, owner_id, title, price_per_night, county, listing_description, img_url
"""

def test_listing_construct():
    listing = Listing(1, 2, '2 bed apartment', 100.50, 'Hertfordshire', 'lovely stay with breakfast included', 'https://tinyurl.com/ye23e59b')

    assert listing.id == 1
    assert listing.owner_id == 2
    assert listing.title =='2 bed apartment'
    assert listing.price_per_night == 100.50
    assert listing.county == 'Hertfordshire'
    assert listing.listing_description == 'lovely stay with breakfast included'
    assert listing.img_url == 'https://tinyurl.com/ye23e59b'

"""
Listing object formats nicely as a string
"""

def test_listing_formats_nicely():
    listing = Listing(1, 2, '2 bed apartment', 100.50, 'Hertfordshire', 'lovely stay with breakfast included', 'https://tinyurl.com/ye23e59b')

    assert str(listing) == "Listing(1, 2, 2 bed apartment, 100.5, Hertfordshire, lovely stay with breakfast included, https://tinyurl.com/ye23e59b)"

"""
Listing objects created with identical parameters are equal
"""

def test_listing_equals_similiar_listing():
    listing = Listing(1, 2, '2 bed apartment', 100.50, 'Hertfordshire', 'lovely stay with breakfast included', 'https://tinyurl.com/ye23e59b')
    listing2 = Listing(1, 2, '2 bed apartment', 100.50, 'Hertfordshire', 'lovely stay with breakfast included', 'https://tinyurl.com/ye23e59b')

    assert listing == listing2