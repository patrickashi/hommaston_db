from rest_framework import serializers
from .models import FormData

class FormDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = FormData
        fields = ['firstname', 'lastname', 'email', 'address', 'phone_number', 'message']
