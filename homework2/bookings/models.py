from typing import Any
from django.db import models
from django.urls import reverse

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=200, help_text="Title of the movie")
    description = models.TextField(max_length=1000, help_text="Description of the movie")
    ## Release date can be null to account for TBA / TBD movies
    release_date = models.DateField(null=True, blank=True)
    duration = models.IntegerField()

    def __str__(self) -> str:
        return self.title
    
class Seat(models.Model):
    seat_number = models.IntegerField(help_text="The given seat number in the theater")
    booking_status = models.CharField(max_length=100, help_text="Whether a seat is currently booked or available")
    seat_price = models.FloatField(help_text="Price of the seat")

    def __str__(self) -> str:
        return str(self.seat_number)
    
class Booking(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    seat = models.ForeignKey(Seat, on_delete=models.CASCADE)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    booking_date = models.DateField(auto_now_add=True)
    show_time = models.TimeField()

    def __str__(self) -> str:
        return self.customer_name
