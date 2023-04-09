from django.shortcuts import render
from rest_framework.views import APIView
# import httpResponse and jsonResponse
from django.http import HttpResponse, JsonResponse
from .models import Stay
from typing import TypedDict
from .customClasses import ResponseBodyGetStays
from .services import rooms_services
from .generalFns.generalFns import makeDateTimeZoneAware
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import authentication_classes


class TestConnection(APIView):

    def get(self, request, *args, **kwargs):
        return HttpResponse("Connection Successful. Server is live on PORT 8000!")


class GetAvailableRooms(APIView):
    authentication_classes = [] #disables authentication
    permission_classes = [] #disables permission
    
    def get(self, request, *args, **kwargs) -> JsonResponse:
        
        if ('startDate' not in request.GET) or ('endDate' not in request.GET) or (request.GET.get('startDate') == '') or (request.GET.get('endDate') == '') or (type(request.GET.get('startDate')).__name__ != 'str')  or (type(request.GET.get('endDate')).__name__ != 'str'):
            return JsonResponse({'msg': 'Please provide the start and end date in the request params'}, status=400)
        
        if 'totalGuests' not in request.GET:
            return JsonResponse({'msg': 'Please provide the total amount of guests in the request params.'}, status=400)

        
        startDateQuery: str = request.GET.get('startDate')
        endDateQuery: str = request.GET.get('endDate')
        totalGuests: int = int(request.GET.get('totalGuests'))
        availableRooms = rooms_services.getAvailableRooms(makeDateTimeZoneAware(startDateQuery), makeDateTimeZoneAware(endDateQuery))
    
        return JsonResponse({'availableRooms': availableRooms}, status=200)
    
class GetUserReservations(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs) -> JsonResponse:
        
        return JsonResponse({ "msg": "Past, present, and future reservations were received." })


class Rooms(APIView):
    

    def post(self, request, *args, **kwargs) -> JsonResponse:


        return JsonResponse({ "msg":"New rooms were added to the database."})
    

    def post(self, request, *args, **kwargs) -> JsonResponse:


        return JsonResponse({ "msg": "Target rooms were updated." })
        
        

        
