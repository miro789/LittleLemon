from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics, viewsets
from rest_framework.permissions import IsAuthenticated
from .models import MenuItem, Booking
from .serializers import MenuSerializer, BookingSerializer, UserSerializer


# Create your views here.
def index(request):
    return render(request, "index.html", {})

def menu_list(request):
    # menu_items = MenuItem.objects.all()
    return render(request, "menu_list.html", {})

def booking(request):
    return render(request, "booking.html", {})

class UserViewSet(viewsets.ModelViewSet):
    """
    Handles GET, POST, PUT, PATCH and DELETE requests for a single Booking.
    """

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]


class MenuItemView(generics.ListCreateAPIView):
    """
    Handles GET and POST requests for MenuItem.
    """

    queryset = MenuItem.objects.all()
    serializer_class = MenuSerializer
    permission_classes = [IsAuthenticated]


class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    """
    Handles GET, PUT, and DELETE requests for a single MenuItem.
    """

    queryset = MenuItem.objects.all()
    serializer_class = MenuSerializer
    permission_classes = [IsAuthenticated]


class BookingViewSet(viewsets.ModelViewSet):
    """
    Handles GET, POST, PUT, PATCH and DELETE requests for a single Booking.
    """

    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]
