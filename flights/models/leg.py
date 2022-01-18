""" Leg models """

# Django
from django.db import models
from flights.models import Airport, Airline
from flights.models.itinerary import Itinerary


class Leg(models.Model):
    """ leg model """
    departure_airport = models.ForeignKey(Airport, on_delete=models.PROTECT, related_name='%(class)s_departure_airport')
    arrival_airport = models.ForeignKey(Airport, on_delete=models.PROTECT, related_name='%(class)s_arrival_airport')
    airline = models.ForeignKey(Airline, on_delete=models.PROTECT, related_name='airline')
    itinerary = models.ForeignKey(Itinerary, on_delete=models.PROTECT, related_name='legs')
    departure_time = models.DateTimeField(
        verbose_name='departure_time'
    )
    arrival_time = models.DateTimeField(
        verbose_name='arrival_time'
    )
    duration = models.IntegerField( null=False, default=60,)
    stops = models.IntegerField( null=False, default=0)

    def __str__(self):
        """ Return leg """
        return str(self.airline.name)

    REQUIRED_FIELDS = ['departure_airport','arrival_airport','airline','departure_time','arrival_time','duration']
