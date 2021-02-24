from rest_framework import serializers


class AddProductSerializer(serializers.Serializer):

    name = serializers.CharField()
    details = serializers.DictField()


class GetProductSerializer(serializers.Serializer):

    name = serializers.CharField()
    details = serializers.DictField()
