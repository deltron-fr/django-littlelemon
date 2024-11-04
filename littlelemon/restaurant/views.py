from django.shortcuts import render
from rest_framework.decorators import api_view
from .models import Menu, Booking
from .serialisers import MenuSerializers, BookingSerializer
from rest_framework import generics, viewsets
from rest_framework.permissions import IsAuthenticated

def index(request):
    return render(request, 'index.html', {})

class MenuItemsView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializers

class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializers

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]