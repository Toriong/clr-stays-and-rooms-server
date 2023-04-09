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




def get_available_rooms(start_date_query: datetime, end_date_query: datetime) -> list[str]:
    unavailable_rooms = Stay.objects.filter(startDate__lte=end_date_query, endDate__gte=start_date_query)

    if len(unavailable_rooms) == 0:
        return ROOMS
    
    unavailable_room_names = [room.roomName for room in unavailable_rooms]
    available_rooms = [room for room in ROOMS if room not in unavailable_room_names]

    return available_rooms