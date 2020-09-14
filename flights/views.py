
from rest_framework.generics import ListAPIView
from .models import Flight, Booking
from .serializers import FlightListSerializer, BookingListSerializer

import datetime

class FlightsList(ListAPIView):
    queryset = Flight.objects.all()
    serializer_class = FlightListSerializer

class Bookings(ListAPIView):
    queryset = Booking.objects.filter(date__gt=datetime.datetime.now())
    serializer_class = BookingListSerializer
