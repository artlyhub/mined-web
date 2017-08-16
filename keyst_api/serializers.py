from rest_framework import serializers
from .models import KeystData


class KeystDataSerializer(serializers.ModelSerializer):

    class Meta:
        model = KeystData
        fields = ('field_name', 'field_data', 'updated')
