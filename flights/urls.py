""" Users URLs. """

# Django
from django.urls import path

# Views
from flights.views import ItinerariesAPIView

urlpatterns = [
    path('flights/itineraries/', ItinerariesAPIView.as_view(), name='itineraries_view'),
]
