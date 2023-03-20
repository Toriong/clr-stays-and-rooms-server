from django.shortcuts import render
from rest_framework.views import APIView
# import httpResponse and jsonResponse
from django.http import HttpResponse, JsonResponse
from .models import Stay
from typing import TypedDict
from .customClasses import ResponseBodyGetStays

# Create your views here.


class TestConnection(APIView):

    def get(self, request, *args, **kwargs):
        return HttpResponse("Connection Successful. Server is live on PORT 8000!")

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

class GetStays(APIView):

    def get(self, request, *args, **kwargs) -> JsonResponse:

        if ('startDate' not in request.GET) or ('endDate' not in request.GET):
            return JsonResponse({'msg': 'Please provide the start and end date in the request params'}, status=400)

        # put the following into a service folder
        startDateQuery = request.GET.get('startDate')
        endDateQuery = request.GET.get('endDate')
        unavailableRooms = Stay.objects.filter(startDate__lte=endDateQuery, endDate__gte=startDateQuery)

        # BRAIN DUMP:
        # get all of the rooms that are taken (unavailableRooms array), using the availableRooms array, filter through the ROOMS array. If the room is in the unavailableRooms array, then remove that room. Return the results to the user in a JSON response.   

        

        
        

        
