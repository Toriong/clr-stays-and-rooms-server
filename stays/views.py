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
    {"name":  "MAIN_HOUSE_DELUXE", "availableRooms": 2},
    {"name": "MAIN_HOUSE_SUPREME", "availableRooms": 1},
    {"name": "COTTAGE_NALIA", "availableRooms": 1},
    {"name": "COTTAGE_SIMBA", "availableRooms": 1},
    {"name": "DORMITORY", "availableRooms": 2},
    {"name": "DELUXE", "availableRooms": 2},
    { "name": "FAMILY", "availableRooms": 2},
]


class GetStays(APIView):

    def get(self, request, *args, **kwargs) -> JsonResponse:
        
        if ('startDate' not in request.GET) or ('endDate' not in request.GET):
            return JsonResponse({'msg': 'Please provide the start and end date in the request params'}, status=400)

        startDateQuery = request.GET.get('startDate')
        endDateQuery = request.GET.get('endDate')
        unavailableRooms = Stay.objects.raw("""SELECT * FROM stays_stay 
                                                WHERE startDate <= %s AND endDate >= %s""", [startDateQuery, endDateQuery])
        unavailableRooms = [room["roomType"] for room in unavailableRooms]
        rooms = {"STANDARD": 0, "FAMILY": 0, "DELUXE": 0, "PREMIUM": 0}

        

        
        

        
