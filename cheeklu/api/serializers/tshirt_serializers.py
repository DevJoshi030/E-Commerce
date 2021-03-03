from rest_framework import serializers


class AddTShirtSerializer(serializers.Serializer):

    name = serializers.CharField()
    price = serializers.CharField()
    description = serializers.CharField()
    quantity = serializers.IntegerField()
    size = serializers.ListField()
    details = serializers.DictField()


class GetTShirtSerializer(serializers.Serializer):

    name = serializers.CharField()
    price = serializers.CharField()
    description = serializers.CharField()
    quantity = serializers.IntegerField()
    size = serializers.ListField()
    details = serializers.DictField()
