from lib.listing import Listing

class ListingRepository():
    def __init__(self, connection):
        self._connection = connection


    def all(self):
        rows = self._connection.execute('SELECT * from listings')
        listings = []
        for row in rows:
            item = Listing(row["id"], row["owner_id"], row["title"], row["price_per_night"],row["county"], row["listing_description"],row["img_url"])
            listings.append(item)
        return listings