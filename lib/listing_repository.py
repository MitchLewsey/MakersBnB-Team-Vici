from lib.listing import Listing

class ListingRepository():
    def __init__(self, connection):
        self._connection = connection

    def all(self):
        rows = self._connection.execute('SELECT * FROM listings')
        listings = []
        for row in rows:
            item = Listing(row["id"], row["owner_id"], row["title"], row["price_per_night"],row["county"], row["listing_description"],row["img_url"])
            listings.append(item)
        return listings
    
    def find(self, id):
        rows = self._connection.execute('SELECT * FROM listings WHERE id = %s',[id])
        if not rows:
            return None
        return Listing(rows[0]["id"], rows[0]["owner_id"], rows[0]["title"], rows[0]["price_per_night"],rows[0]["county"], rows[0]["listing_description"],rows[0]["img_url"])
    
    def create(self, listing):
        rows = self._connection.execute("INSERT INTO listings (owner_id, title, price_per_night, county, listing_description, img_url)" \
        "VALUES(%s, %s, %s, %s, %s, %s) RETURNING id", 
        [listing.owner_id, listing.title, listing.price_per_night, listing.county, listing.listing_description, listing.img_url])
        
        listing.id = rows[0]["id"]
        return listing