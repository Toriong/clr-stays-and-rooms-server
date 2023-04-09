from typing import TypedDict, List

class RoomReqBodyData(TypedDict):
    ui_name: str
    description: str
    amenities: List[str]

class RoomReqInfo(RoomReqBodyData):
    name: str

