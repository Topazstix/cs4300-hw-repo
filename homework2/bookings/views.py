# from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.views import generic
from rest_framework import viewsets
import requests
from .models import *
from .serializers import *

# Create your views here.
class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class SeatViewSet(viewsets.ModelViewSet):
    queryset = Seat.objects.all()
    serializer_class = SeatSerializer

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer


def index(request: HttpResponse) -> HttpResponse:
    return render(request, 'bookings/base.html')

# def api(request: HttpResponse) -> HttpResponse:
    
#     return redirect('index')

def movie_list(request: HttpResponse) -> HttpResponse:
    ## It wasnt im a dodo. fixed by grabbing context instead for Movie object
    movies = Movie.objects.all()
    return render(request, 'bookings/movie_list.html', {'movies': movies})

def book_seat(request: HttpResponse, movie_id: int) -> HttpResponse:
    movie = get_object_or_404(Movie, id=movie_id)
    seats = Seat.objects.filter(booking_status='available')
    return render(request, 'bookings/seat_booking.html', {'movie': movie, 'seats': seats})

def confirm_booking(request: HttpResponse, movie_id: int, seat_id: int) -> HttpResponse:
    movie = get_object_or_404(Movie, id=movie_id)
    seat = get_object_or_404(Seat, id=seat_id)
    
    ## Handle post requests for booking ops
    ### NOTE: REQUIRES user auth, which is currently not configured.
    if request.method == 'POST':
        Booking.objects.create(movie=movie, seat=seat, user=request.user)
        seat.booking_status = 'booked'
        seat.save()
        return redirect('booking_history')
    return render(request, 'bookings/confirm_booking.html', {'movie': movie, 'seat': seat})

def seat_booking(request: HttpResponse) -> HttpResponse:
    seats = Seat.objects.filter(booking_status='available')
    return render(request, 'bookings/seat_booking.html', {'seats': seats})

def booking_history(request: HttpResponse) -> HttpResponse:
    bookings = Booking.objects.all()
    return render(request, 'bookings/booking_history.html', {'bookings': bookings})