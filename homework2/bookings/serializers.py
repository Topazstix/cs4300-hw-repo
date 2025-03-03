from rest_framework import serializers
from .models import Booking, Movie, Seat

"""
rest_framework.serializer methodology to make easy conversion of model data into JSON format for API endpoints
using references from the django rest framework docs (https://www.django-rest-framework.org/api-guide/serializers/)
and just declaring '__all__' fields for serialization. Will adjust if necessary as per data requirements
"""

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'
        
class SeatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seat
        fields = '__all__'
        
class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'
        
