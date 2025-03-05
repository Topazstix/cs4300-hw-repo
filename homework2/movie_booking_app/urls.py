"""
URL configuration for movie_booking_app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
# from bookings.views import index, movie_list, book_seat, confirm_booking, booking_history
from bookings.views import *

## Instantiate the rest_framework router
router = DefaultRouter()

## Register the viewsets
router.register(r'movies', MovieViewSet)
router.register(r'seats', SeatViewSet)
router.register(r'bookings', BookingViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    ## Initialize standard `api/*` endpoints
    ### Example: `api/movies/` for the default movies endpoint
    path('api/', include(router.urls)),

    ## Base endpoints
    path('movies/', movie_list, name='movies'),
    path('seats/', seat_booking, name='seats'),
    path('bookings/', booking_history, name='bookings'),

    ## CRUD Ops endpoints
    ### NOTE: Not exactly operational, template paths currently for UI
    path('book_seat/<int:movie_id>/', book_seat, name='book_seat'),
    path('confirm_booking/<int:movie_id>/<int:seat_id>/', confirm_booking, name='confirm_booking'),
    path('booking_history/', booking_history, name='booking_history'),
]
