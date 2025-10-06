from enum import Enum

class DriverStatus(Enum):
    ONLINE = 'online'
    OFFLINE = 'offline'
    BUSY = 'busy'
    FREE = 'free'