""" Itineraries views. """

# Django REST Framework
from rest_framework.views import APIView
from rest_framework.response import Response

# Serializers
from flights.serializers import ItineraryModelSerializer, LegModelSerializer

# filter
from flights.filters import *

# Models
from flights.models import Itinerary, Leg

class ItinerariesAPIView(APIView):
    def get(self, request, *args, **kwargs):
        airline_name = request.GET.get('airline')        
        if airline_name == None:
            legs = Leg.objects.all()
            itineraries = Itinerary.objects.all()
        else:
            legs = Leg.objects.filter(airline__name=airline_name)
            itineraries = Itinerary.objects.filter(agent__airline__name=airline_name)

        legs_serializer = LegModelSerializer(legs, many = True)
        itineraries_serializer = ItineraryModelSerializer(itineraries, many = True)

        response = {
            'itineraries' : itineraries_serializer.data,
            'legs': legs_serializer.data
        }

        return Response(response)

