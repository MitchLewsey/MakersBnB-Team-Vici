class Listing():
    def __init__(self,id, owner_id, title, price_per_night, county, listing_description, img_url):
        self.id = id
        self.owner_id = owner_id
        self.title = title
        self.price_per_night = price_per_night
        self.county = county
        self.listing_description = listing_description
        self.img_url = img_url

    def __repr__(self):
        return f"Listing({self.id}, {self.owner_id}, {self.title}, {self.price_per_night}, {self.county}, {self.listing_description}, {self.img_url})"

    def __eq__(self, other):
        return self.__dict__ == other.__dict__