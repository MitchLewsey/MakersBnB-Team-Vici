class Bookings():
    def __init__(self,id,guest_id,listing_id,start_date,end_date,checkout_date,price): 
        self.id = id 
        self.guest_id = guest_id
        self.listing_id = listing_id
        self.start_date = start_date
        self.end_date = end_date
        self.checkout_date = checkout_date
        self.price = price

    def __eq__(self, value):
        return self.__dict__ == value.__dict__ 