from driver_status import DriverStatus 
from ride_status import RideStatus
from user import User

class Driver(User):
    def __init__(self, name, email, phone, user_id, current_location, driver_id, driver_status=DriverStatus.OFFLINE):
        super().__init__(name, email, phone, user_id, current_location)
        self.driver_id = driver_id
        self.driver_status = driver_status
        self.current_ride_status = None  # Track the current ride request

    def set_availability(self, status):
        if isinstance(status,DriverStatus):
            self.driver_status = status
    
    def receive_ride_request(self, ride_status=RideStatus.REQUESTED):
        self.current_ride_status = ride_status

    def accept_ride(self):
        self.current_ride_status = RideStatus.ACCEPTED
        print("Ride accepted.")
    
    def cancel_ride(self):
        self.current_ride_status = RideStatus.CANCELLED
        print("Ride cancelled.")

    def start_ride(self):
        self.current_ride_status = RideStatus.STARTED

    def navigate_to_location(self,location):
        print(f"Navigating to {location}.")

    def confirm_pickup(self):
        self.current_ride_status = RideStatus.PICK_UP
        print("Pickup confirmed.")

    def complete_trip(self):
        self.current_ride_status = RideStatus.COMPLETED
        print("Trip completed.")
