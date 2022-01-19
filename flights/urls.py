""" Users URLs. """

# Django
# from django.urls import path
from django.conf.urls import url

# Views
from flights.views import ItinerariesAPIView

urlpatterns = [
    url('flights/itineraries/', ItinerariesAPIView.as_view(), name='itineraries_view'),
]

