from rest_framework.views import APIView
from django.http import HttpResponse, JsonResponse, HttpRequest
from .services import admin_rooms_services
from rest_framework.permissions import IsAuthenticated
from .customTypes import RoomReqInfo

# Create your views here.


class Rooms(APIView):
    authentication_classes = [] #disables authentication
    permission_classes = [] #disables permission


    def post(self, request) -> JsonResponse:


        return JsonResponse({ "msg": "New room was posted." })
    

    def put(self, request: HttpRequest) -> JsonResponse:
        # GOAL: get the file from the request, store it onto the server, when done, delete immediately
        # BRAIN DUMP:
        # check if the user uploaded a file to the server 
        reqInfo: RoomReqInfo = request.data

        if reqInfo['request_name'] == 'add_photos':
            admin_rooms_services.upload_photos(request.FILES)


        
        return JsonResponse({ "msg": "Updates occurred successfully for target room "})