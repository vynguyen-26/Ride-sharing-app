from enum import Enum

class RideStatus(Enum):
    REQUESTED = 'requested'
    ACCEPTED = 'accepted'
    STARTED = 'started'
    PICK_UP = 'pick_up'
    COMPLETED = 'complete'
    CANCELLED = 'cancelled'