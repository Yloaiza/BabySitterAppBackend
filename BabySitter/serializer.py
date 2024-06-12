from rest_framework import serializers
from .models import User,Nanny,Reservation

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields= '__all__'

class NannySerializer(serializers.ModelSerializer):
    class Meta:
        model = Nanny
        fields= '__all__'

class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields= '__all__'