from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from bookings.models import Movie, Seat
from rest_framework.test import APIClient

"""
Using djangos testcase models for testing via API endpoints

NOTE: User auth is handled thru raw django models atm

TESTS RAN:
    Movie Models:
        - Movie List
        - Movie Create
    Booking Models:
        - Booking List
        - Booking Create
    Seat Models:
        - Seat List
        - Seat Create
"""

class MovieAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_movie_list(self):
        response = self.client.get(reverse('movie-list'))
        self.assertEqual(response.status_code, 200)

    def test_movie_create(self):
        response = self.client.post(reverse('movie-list'), {
            'title': 'Test Movie',
            'description': 'Test Description',
            'release_date': '2023-01-01',
            'duration': 120
        })
        self.assertEqual(response.status_code, 201)

class BookingAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.movie = Movie.objects.create(
            title='Test Movie', 
            description='Test Description', 
            release_date='2023-01-01', 
            duration=120
        )
        self.seat = Seat.objects.create(
            seat_number=1, 
            booking_status='available', 
            seat_price=10.0
        )

    def test_booking_list(self):
        response = self.client.get(reverse('booking-list'))
        self.assertEqual(response.status_code, 200)

    def test_booking_create(self):
        response = self.client.post(reverse('booking-list'), {
            'user': self.user.id,
            'movie': self.movie.id,
            'seat': self.seat.id,
            'show_time': '19:00'
        })
        self.assertEqual(response.status_code, 201)

class SeatAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_seat_list(self):
        response = self.client.get(reverse('seat-list'))
        self.assertEqual(response.status_code, 200)

    def test_seat_create(self):
        response = self.client.post(reverse('seat-list'), {
            'seat_number': 1,
            'booking_status': 'available',
            'seat_price': 10.0
        })
        self.assertEqual(response.status_code, 201)