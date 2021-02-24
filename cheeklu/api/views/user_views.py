from ..serializers.user_serializers import AddUserSerializer, \
    LoginUserSerializer

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from django.contrib.auth.hashers import check_password, make_password

# MongoDB
import json
import pymongo

f = open("admin_uri.json", 'r')
srv = json.loads(f.read())
client = pymongo.MongoClient(srv['uri'])

# API Views


class AddUser(APIView):

    serializer_class = AddUserSerializer

    def post(self, request, format=None):

        serializer = self.serializer_class(data=request.data)

        if not serializer.is_valid():

            return Response({"Error": "error"},
                            status=status.HTTP_400_BAD_REQUEST)

        name = serializer.validated_data.get('name')
        user_id = serializer.validated_data.get('user_id')
        password = serializer.validated_data.get('password')

        password = make_password(password)

        db = client['Test']

        collection = db['users']

        collection.insert_one({
            'name': name,
            'user_id': user_id,
            'password': password
        })

        return Response({"Success": "User Added!"}, status=status.HTTP_200_OK)


class LoginUser(APIView):

    serializer_class = LoginUserSerializer

    def post(self, request, format=None):

        serializer = self.serializer_class(data=request.data)

        if not serializer.is_valid():

            return Response({"Error": "error"},
                            status=status.HTTP_400_BAD_REQUEST)

        user_id = serializer.validated_data.get('user_id')
        password = serializer.validated_data.get('password')

        db = client['Test']

        collection = db['users']

        user = collection.find_one({
            "user_id": user_id
        })

        if not user:
            return Response({"Error": "error"},
                            status=status.HTTP_401_UNAUTHORIZED)

        password_db = user['password']

        if check_password(password, password_db):

            return Response({"Success": "Login Successful!"},
                            status=status.HTTP_200_OK)

        return Response({"Error": "error"},
                        status=status.HTTP_401_UNAUTHORIZED)
