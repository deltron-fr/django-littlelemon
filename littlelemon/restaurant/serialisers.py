from django.contrib.auth.models import User
from .models import Menu, Booking
from rest_framework import serializers

class MenuSerializers(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = ['Title', 'Price', 'Inventory']

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ["Name", "No_of_guest", "BookingDate"]
