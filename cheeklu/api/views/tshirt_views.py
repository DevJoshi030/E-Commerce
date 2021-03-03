from ..serializers.tshirt_serializers import AddTShirtSerializer, \
    GetTShirtSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# MongoDB
import json
import pymongo

f = open("admin_uri.json", 'r')
srv = json.loads(f.read())
client = pymongo.MongoClient(srv['uri'])

# Constants
DB_NAME = 'Cheeklu-Gifts'
COLLECTION_NAME = 'TShirts'

# DB and Collection

db = client[DB_NAME]
collection = db[COLLECTION_NAME]

# API Views


class AddTShirt(APIView):

    serializer_class = AddTShirtSerializer

    def post(self, request, format=None):

        serializer = self.serializer_class(data=request.data)

        if not serializer.is_valid():

            return Response({"Error": "error"},
                            status=status.HTTP_400_BAD_REQUEST)

        name = serializer.validated_data.get('name')
        price = serializer.validated_data.get('price')
        description = serializer.validated_data.get('description')
        quantity = serializer.validated_data.get('quantity')
        size = serializer.validated_data.get('size')
        details = serializer.validated_data.get('details')

        collection.insert_one({
            "name": name,
            "price": price,
            "description": description,
            "quantity": quantity,
            "size": size,
            "details": details
        })

        return Response({"Success": "Done"}, status=status.HTTP_200_OK)


class GetTShirt(APIView):

    serializer_class = GetTShirtSerializer

    def get(self, request, format=None, **kwargs):

        name = kwargs['name']

        data = self.serializer_class(collection.find_one({"name": name})).data

        return Response({"Data": data}, status=status.HTTP_200_OK)
