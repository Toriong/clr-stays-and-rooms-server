from .customTypes import ResBodyGetStaysDict
from dataclasses import dataclass


@dataclass
class ResponseBodyGetStays:
    premiumRoomsAvailable: int
    deluxeRoomsAvailable: int
    familyRoomsAvailable: int
    standardRoomsAvailable: int

    def convertToJson(self) -> ResBodyGetStaysDict:
        return {
            "premiumRoomsAvailable": self.premiumRoomsAvailable,
            "deluxeRoomsAvailable": self.deluxeRoomsAvailable,
            "familyRoomsAvailable": self.familyRoomsAvailable,
            "standardRoomsAvailable": self.standardRoomsAvailable
        }