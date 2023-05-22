from rest_framework import serializers
from app.models import *
from .models import *
from app.forms import *


class SigninSerializer(serializers.ModelSerializer):
    class Meta:
        model = Signin
        fields = '__all__'


class SignupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Signup
        fields = '__all__'


class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = '__all__'
