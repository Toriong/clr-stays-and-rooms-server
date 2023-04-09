from datetime import datetime
from stays.models import Stay

ROOMS = [
    "MAIN_HOUSE_DELUXE_1",
    "MAIN_HOUSE_DELUXE_2",
    "MAIN_HOUSE_SUPREME",
    "COTTAGE_NALIA",
    "COTTAGE_SIMBA",
    "DORMITORY_1",
    "DORMITORY_2",
    "DELUXE_1",
    "DELUXE_2",
    "FAMILY_1",
    "FAMILY_2",
]

# CASE: there are less than 5 people in the party. 
# GOAL: don't get the dorm rooms or the family rooms 

# GOAL: insert the json field into the database for the available rooms 




def getAvailableRooms(startDateQuery: datetime, endDateQuery: datetime) -> list[str]:
    unavailableRooms = Stay.objects.filter(startDate__lte=endDateQuery, endDate__gte=startDateQuery)

    if len(unavailableRooms) == 0:
        return ROOMS
    
    unavailableRoomNames = [room.roomName for room in unavailableRooms]
    availableRooms = [room for room in ROOMS if room not in unavailableRoomNames]

    return availableRooms