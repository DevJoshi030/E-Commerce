from rest_framework import serializers


class GetFormDataSerializer(serializers.Serializer):

    category = serializers.CharField()
    main_data = serializers.ListField()
    details_data = serializers.ListField()
