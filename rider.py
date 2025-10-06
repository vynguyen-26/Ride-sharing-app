from enums import RiderStatus, RideStatus
from user import User

class Rider(User):
    def __init__(self, name, email, phone, user_id, current_location, rider_id, rider_status=RiderStatus.LOOKING):
        super().__init__(name, email, phone, user_id, current_location)
        self.rider_id = rider_id
        self.rider_status = rider_status
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

    def track_driver_location(self):
        if self.current_driver:
            print(f"Driver location: {self.current_driver.current_location}")
        else:
            print("No driver assigned.")