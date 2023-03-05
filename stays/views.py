from django.shortcuts import render
from rest_framework.views import APIView
# import httpResponse and jsonResponse
from django.http import HttpResponse, JsonResponse

# Create your views here.


class TestConnection(APIView):

    def get(self, request, *args, **kwargs):
        return HttpResponse("Connection Successful. Server is live on PORT 8000!")
    


class GetStays(APIView):

    def get(self, request, *args, **kwargs):
        pass
