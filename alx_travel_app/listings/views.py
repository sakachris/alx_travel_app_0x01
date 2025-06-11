# listings/views.py
from rest_framework import viewsets
from .models import Property, Booking
from .serializers import PropertySerializer, BookingSerializer


class PropertyViewSet(viewsets.ModelViewSet):
    """
    ViewSet for managing Property instances.

    Provides standard CRUD actions (list, retrieve, create, update, delete)
    for the Property model.
    """

    queryset = Property.objects.all()
    serializer_class = PropertySerializer


class BookingViewSet(viewsets.ModelViewSet):
    """
    ViewSet for managing Booking instances.

    Provides standard CRUD actions (list, retrieve, create, update, delete)
    for the Booking model.
    """

    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
