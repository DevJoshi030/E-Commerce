from ..serializers.form_data_serializers import GetFormDataSerializer
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
COLLECTION_NAME = 'Form Data'

# DB and Collection

db = client[DB_NAME]
collection = db[COLLECTION_NAME]

# API Views


class GetFormData(APIView):

    serializer_class = GetFormDataSerializer

    def get(self, request, format=None, **kwargs):

        category = kwargs["category"]

        queryset = collection.find_one({"category": category})

        if not queryset:
            return Response({"Error": "Wrong Category"}, status=status.HTTP_400_BAD_REQUEST)

        data = self.serializer_class(queryset).data

        return Response({"Data": data}, status=status.HTTP_200_OK)
