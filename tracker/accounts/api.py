from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response


class Accounts(APIView):

    def post(self, request, *args, **kwargs):
        print(request.data["name"])
        return Response("OK Working")
