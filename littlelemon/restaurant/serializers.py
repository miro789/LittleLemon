from .models import MenuItem, Booking
from rest_framework import serializers

# from django.contrib.auth.models import User


class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        # fields = ["url", "title_menu", "price", "inventory"]
        fields = "__all__"


# class UserSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = User
#         fields = ["url", "username", "email", "groups"]


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = "__all__"
