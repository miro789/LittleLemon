from .models import MenuItem, Booking
from django.contrib.auth.models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        # fields = ["url", "title_menu", "price", "inventory"]
        fields = "__all__"


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = "__all__"
