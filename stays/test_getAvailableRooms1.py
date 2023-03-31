from django.test import TestCase
from .models import Stay
from rest_framework.test import APIClient
from django.urls import reverse
from django.utils.timezone import make_aware
from datetime import datetime


# insert the dummy data, the stays, the user should get the following back:
# "MAIN_HOUSE_DELUXE_2", "COTTAGE_SIMBA", "DELUXE_1", "FAMILY_1", 

ROOMS_ALL = [
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


class GetAvailableRoomsTest1(TestCase):
    client = APIClient()
    unavailableRooms = ["MAIN_HOUSE_DELUXE_2", "COTTAGE_SIMBA", "DELUXE_1"]

    def setUp(self):
        """
        Insert the testing data into the database
        """
        testingDataStays = ["MAIN_HOUSE_DELUXE_2", "COTTAGE_SIMBA", "DELUXE_1"]
        dtDictStartDate = datetime.strptime("2023-03-20", "%Y-%m-%d")
        dtDictEndDate = datetime.strptime("2023-03-27", "%Y-%m-%d")

        for stay in testingDataStays:
            Stay.objects.create(
                startDate = make_aware(dtDictStartDate),
                endDate = make_aware(dtDictEndDate),
                adultsNum = 2,
                childrenNum = 2,
                roomName = stay,
            )

        Stay.objects.create(startDate = make_aware(dtDictStartDate), endDate = make_aware(dtDictEndDate), adultsNum = 2, childrenNum = 2, roomName = "FAMILY_1")


    def test_getAvailableRooms(self):
        """
        Tests the getAvailableRooms function
        """
        response = self.client.get(reverse('get-available-rooms'), {'startDate': '2023-03-20', 'endDate': '2023-03-25'})
        self.assertEqual(response.status_code, 200)
        fromServer = response.json()
        availableRooms = fromServer['availableRooms']
        print("availableRooms: ", availableRooms)
        # all of the elements in availableRooms should not be in unavailableRooms
        for room in availableRooms:
            self.assertNotIn(room, self.unavailableRooms)


    def tearDown(self):
        print("Test has ended.")
        """
        Tears down the test environment
        """

    
    
