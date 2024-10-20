from django.shortcuts import render
from rest_framework import generics, viewsets, permissions
from .models import MenuItem, Booking
from .serializers import MenuSerializer, BookingSerializer


# Create your views here.
def index(request):
    return render(request, "index.html", {})


class MenuItemView(generics.ListCreateAPIView):
    """
    Handles GET and POST requests for MenuItem.
    """

    queryset = MenuItem.objects.all()
    serializer_class = MenuSerializer
    # permission_classes = [permissions.IsAuthenticated]


class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    """
    Handles GET, PUT, and DELETE requests for a single MenuItem.
    """

    queryset = MenuItem.objects.all()
    serializer_class = MenuSerializer
    # permission_classes = [permissions.IsAuthenticated]


class BookingViewSet(viewsets.ModelViewSet):
    """
    Handles GET, POST, PUT, PATCH and DELETE requests for a single Booking.
    """

    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    # permission_classes = [permissions.IsAuthenticated]
