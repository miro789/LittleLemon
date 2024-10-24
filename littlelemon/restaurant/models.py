from django.db import models


# Create your models here.
class MenuItem(models.Model):
    id = models.AutoField(primary_key=True)
    title_menu = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    inventory = models.SmallIntegerField()
    image_name = models.CharField(max_length=100, blank=True) # Use image_name

    class Meta:
        ordering = ["title_menu"]

    def __str__(self):
        return f"{self.title_menu}: {str(self.price)}"  # Output: "Pizza : 9.99"


class Booking(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    no_of_guests = models.SmallIntegerField()
    bookingDate = models.DateTimeField()

    class Meta:
        ordering = [
            "-bookingDate"
        ]  # descending - the most recent bookings will show up first.

    def __str__(self):
        return str(self.name)
