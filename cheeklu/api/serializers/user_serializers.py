from rest_framework import serializers


class AddUserSerializer(serializers.Serializer):

    name = serializers.CharField()
    user_id = serializers.CharField()
    password = serializers.CharField()


class LoginUserSerializer(serializers.Serializer):

    user_id = serializers.CharField()
    password = serializers.CharField()
