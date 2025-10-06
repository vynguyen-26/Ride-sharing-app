from rider_status import RiderStatus 
from ride_status import RideStatus
from user import User

class Rider(User):
    def __init__(self, name, email, phone, user_id, current_location, rider_id, rider_status=RiderStatus.LOOKING):
        super().__init__(name, email, phone, user_id)
        self.rider_id = rider_id
        self.rider_status = rider_status
        self.current_location = current_location
        self.pickup_location = None
        self.dropoff_location = None
        self.current_ride_status = None 
        self.current_driver = None  #Track assigned driver
    
    def request_ride(self, pickup_location, dropoff_location):
        self.pickup_location = pickup_location
        self.dropoff_location = dropoff_location
        self.current_ride_status = RideStatus.REQUESTED
        self.rider_status = RiderStatus.LOOKING
        print("Ride requested. Looking for driver.")
    
    def cancel_ride(self):
        self.current_ride_status = RideStatus.CANCELLED
        self.rider_status = RiderStatus.LOOKING
        self.current_driver = None
        print("Ride cancelled.")
    
    def update_status(self, status):
        if isinstance(status, RiderStatus):
            self.rider_status = status