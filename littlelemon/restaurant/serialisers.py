from django.contrib.auth.models import User
from .models import Menu
from rest_framework import serializers

class MenuSerializers(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = ['Title', 'Price', 'Inventory']