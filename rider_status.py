from enum import Enum

class RiderStatus(Enum):
    LOOKING = 'looking' 
    FOUND_FDRIVER = 'found'
    IN_PROGRESS = 'in_progress'
    COMPLETE = 'completed'