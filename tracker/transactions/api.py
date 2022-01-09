from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.decorators import api_view



class Test(APIView):

    def get(self, request, *args, **kwargs):
        return Response({"message":"Test Api Success","status":status.HTTP_200_OK})