from lib.listing import Listing 

"""
Listing constructs id, owner (fk userid), title, price per night, county, desc, img url
"""

def test_listing_construct():
    listing = Listing(1, 2, '2 bed apartment', 100.50, 'Hertfordshire', 'lovely stay with breakfast included', 'https://tinyurl.com/ye23e59b')

    assert listing.id == 1
    assert listing.owner == 2
    assert listing.title =='2 bed apartment'
    assert listing.price_per_night == 100.50
    assert listing.county == 'Hertfordshire'
    assert listing.desc == 'lovely stay with breakfast included'
    assert listing.img_url == 'https://tinyurl.com/ye23e59b'


def test_listing_formats_nicely():
    listing = Listing(1, 2, '2 bed apartment', 100.50, 'Hertfordshire', 'lovely stay with breakfast included', 'https://tinyurl.com/ye23e59b')

    assert str(listing) == "Listing(1, 2, '2 bed apartment', 100.50, 'Hertfordshire', 'lovely stay with breakfast included', 'https://tinyurl.com/ye23e59b')"