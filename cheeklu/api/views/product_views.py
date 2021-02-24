from ..serializers.product_serializers import AddProductSerializer, \
    GetProductSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# MongoDB
import json
import pymongo

f = open("admin_uri.json", 'r')
srv = json.loads(f.read())
client = pymongo.MongoClient(srv['uri'])


# API Views

class AddProduct(APIView):

    serializer_class = AddProductSerializer

    def post(self, request, format=None):

        serializer = self.serializer_class(data=request.data)

        if not serializer.is_valid():

            return Response({"Error": "error"},
                            status=status.HTTP_400_BAD_REQUEST)

        name = serializer.validated_data.get('name')
        details = serializer.validated_data.get('details')

        db = client.Test

        collection = db["products"]

        collection.insert_one({
            "name": name,
            "details": details
        })

        return Response({"Success": "Done"}, status=status.HTTP_200_OK)


class GetProduct(APIView):

    serializer_class = GetProductSerializer

    def get(self, request, format=None, **kwargs):

        name = kwargs['name']

        db = client.Test

        collection = db["products"]

        data = self.serializer_class(collection.find_one({"name": name})).data

        return Response({"Success": data}, status=status.HTTP_200_OK)
