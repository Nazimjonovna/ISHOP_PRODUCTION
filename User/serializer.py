from rest_framework import serializers
from .models import *
from phonenumber_field.serializerfields import PhoneNumberField



class AdminSerializer(serializers.ModelSerializer):
    phone_number = PhoneNumberField()

    class Meta:
        model = User
        fields = ('phone_number', 'password', 'is_staff', 'is_active', 'is_superuser', 'created_at', 'updated_at')
        read_only_fields = ('created_at', 'updated_at')

    def validate_phone_number(self, value):
        # Additional custom validation can be added here if needed
        return value
    

class LoginSerializer(serializers.ModelSerializer):
    phone_number = PhoneNumberField()

    class Meta:
        model = User
        fields = ('phone_number', 'password', 'created_at', 'updated_at')
        read_only_fields = ('created_at', 'updated_at')

    def validate_phone_number(self, value):
        # Additional custom validation can be added here if needed
        return value
