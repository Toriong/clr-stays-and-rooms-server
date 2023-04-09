from typing import TypedDict, List

class RoomReqBodyData(TypedDict):
    ui_name: str
    description: str
    amenities: List[str]

class RoomReqInfo(RoomReqBodyData):
    request_name: str


class Upload_File_AWS_Result(TypedDict):
    msg: str
    wasSuccessful: bool
