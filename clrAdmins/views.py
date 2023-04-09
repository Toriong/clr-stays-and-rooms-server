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
        print('request.data: ', request.data)
        reqInfo: RoomReqInfo = request.data
        print('reqInfo: ', reqInfo)

        # GOAL: when the user inserts a new photo for a room, perform the folllowing:
        # insert the photo into aws bucket, get the id for the photo
        # for the specific room, insert the id of the photo into the room model

        if reqInfo['requestName'] == 'addPhotos':
            admin_rooms_services.upload_photos(request.FILES)

            return JsonResponse({ "msg": "Updates occurred successfully. New photos were added to the room."})


        
        return JsonResponse({ "msg": "Updates occurred successfully for target room "})