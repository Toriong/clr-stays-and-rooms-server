from django.shortcuts import render
from rest_framework.views import APIView
# import httpResponse and jsonResponse
from django.http import HttpResponse, JsonResponse
from .models import Stay
from typing import TypedDict
from .customClasses import ResponseBodyGetStays
from .services import roomsServices
from .generalFns.generalFns import makeDateTimeZoneAware


class TestConnection(APIView):

    def get(self, request, *args, **kwargs):
        return HttpResponse("Connection Successful. Server is live on PORT 8000!")


class GetAvailableRooms(APIView):

    def get(self, request, *args, **kwargs) -> JsonResponse:
        
        if ('startDate' not in request.GET) or ('endDate' not in request.GET) or (request.GET.get('startDate') == '') or (request.GET.get('endDate') == '') or (type(request.GET.get('startDate')).__name__ != 'str')  or (type(request.GET.get('endDate')).__name__ != 'str'):
            return JsonResponse({'msg': 'Please provide the start and end date in the request params'}, status=400)

        
        startDateQuery: str = request.GET.get('startDate')
        endDateQuery: str = request.GET.get('endDate')
        availableRooms = roomsServices.getAvailableRooms(makeDateTimeZoneAware(startDateQuery), makeDateTimeZoneAware(endDateQuery))
    
        return JsonResponse({'availableRooms': availableRooms}, status=200)

        

        
        

        
