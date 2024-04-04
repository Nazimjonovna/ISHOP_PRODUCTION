from rest_framework import serializers
from .models import *
from phonenumber_field.serializerfields import PhoneNumberField
from django.contrib.auth.hashers import make_password, check_password
from Product.models import *


class SendSmsSerializer(serializers.Serializer):
    phone_number = serializers.IntegerField()
    text = serializers.CharField(max_length=256)

class PhoneSRL(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('phone_number', )

class OtpSRL(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('phone_number', 'otp')

class DataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'

class RegisterUserSerialzier(serializers.ModelSerializer):
    phone_number = PhoneNumberField()
    class Meta:
        model = User
        fields = ['phone_number', 'password', 'otp'] 

    def create(self, validated_data):
        password = validated_data.pop('password')
        hashed_password = make_password(password)
        user = User.objects.create(password=hashed_password, **validated_data)
        return user

class SwaggerRegisterSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    last_name = serializers.CharField(max_length=200)
    card = serializers.IntegerField(allow_null=True)
    card_info = serializers.CharField(max_length=4, allow_null=True)
    paspord_raqam = serializers.CharField(max_length=6, allow_null=True)
    paspord_seria = serializers.CharField(max_length=3, allow_null=True)
    paspord = serializers.ImageField(allow_null=True)
    image = serializers.ImageField(allow_null=True)
    adress = serializers.CharField(allow_null=True)
    viloyat = serializers.CharField(max_length=100)
    phone_number = serializers.CharField(max_length=100)
    password = serializers.CharField(max_length=100)
    otp = serializers.CharField(max_length=100)

class Log(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("phone_number", "password")



class ChangePasswordSerializer(serializers.ModelSerializer):
    old_password = serializers.CharField(required=True, write_only=True)
    new_password = serializers.CharField(required=True, write_only=True)
    password2 = serializers.CharField(required=True, write_only=True)

    class Meta:
        model = User
        fields = ['old_password', 'new_password', 'password2']

    def validate(self, attrs):
        if attrs['new_password'] != attrs['password2']:
            raise serializers.ValidationError({'passwords': "The two password fields didn't match."})
        return attrs

    def update(self, instance, validated_data):
        old_password = validated_data.get('old_password')
        if not check_password(old_password, instance.password):
            raise serializers.ValidationError({'old_password': 'Wrong password'})
        instance.password = make_password(validated_data['new_password'])
        instance.save()
        return instance


class VerifyCodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Verification
        fields = ('phone_number', 'verify_code', 'step_change_phone')
        extra_kwargs = {
            'step_change_phone': {'read_only': True}
        }

    def update(self, instance, validated_data):
        verify_code = validated_data['verify_code']
        if instance.verify_code == verify_code:
            instance.is_verified = True
            if instance.step_reset == 'send':
                instance.step_reset = 'confirmed'
            if instance.step_change_phone:
                if instance.step_change_phone == 'send':
                    instance.step_change_phone = 'confirmed'
            instance.save()
            return instance
        else:
            raise serializers.ValidationError({'error': 'Phone number or verify code incorrect'})


class ResetPasswordSerializer(serializers.ModelSerializer):
    phone_number = serializers.CharField()
    new_password = serializers.CharField()
    re_new_password = serializers.CharField()

    class Meta:
        model = User
        fields = ('phone_number', 'new_password', 're_new_password')

    def validate(self, attrs):
        if not attrs['new_password']:
            raise serializers.ValidationError({'new_password': 'This field is required.'})

        if not attrs['re_new_password']:
            raise serializers.ValidationError({'re_new_password': 'This field is required.'})

        if attrs['new_password'] != attrs['re_new_password']:
            raise serializers.ValidationError({'passwords': "The two password fields didn't match."})

        return attrs




#? ADMIN SERIALIZERS
class AdminSRL(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['phone_number', 'password', 'is_staff', 'is_active', 'is_superuser'] 

    def create(self, validated_data):
        password = validated_data.pop('password')
        hashed_password = make_password(password)
        user = User.objects.create(password=hashed_password, **validated_data)
        return user
    

class Protsentsrl(serializers.ModelSerializer):
    class Meta:
        model = Protsent
        fields = '__all__'

class EditTasdiqsrl(serializers.ModelSerializer):
    name = serializers.CharField(max_length = 200)
    class Meta:
        model = Product
        fields = "__all__"














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
