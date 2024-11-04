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

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "email"]

class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True,
                                    required=True,
                                    style={'input_type': 'password', 'placeholder': 'Password'})
    class Meta:
        model = User
        fields = ["username", "email", "password"]

        def create(self, validated_data):
            user = User(
                username = validated_data["username"],
                email = validated_data["email"],
            )
            user.set_password(validated_data['password']) 
            user.save()
            return user 