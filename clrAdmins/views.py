from rest_framework.views import APIView
from django.http import HttpResponse, JsonResponse
from .services import admin_rooms_services
from rest_framework.permissions import IsAuthenticated

# Create your views here.


class Rooms(APIView):
    authentication_classes = [] #disables authentication
    permission_classes = [] #disables permission


    def post(self, request) -> JsonResponse:


        return JsonResponse({ "msg": "New room was posted." })
    

    def put(self, request) -> JsonResponse:

        admin_rooms_services.upload_photos()
        
        return JsonResponse({ "msg": "Updates occurred successfully for target room "})