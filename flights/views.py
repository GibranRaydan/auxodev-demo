""" Itineraries views. """

# Django REST Framework
from rest_framework.views import APIView
from rest_framework.response import Response

# Serializers
from flights.serializers import ItineraryModelSerializer, LegModelSerializer

# Models
from flights.models import Itinerary, Leg

# import pdb


class ItinerariesAPIView(APIView):

    def get(self, request, *args, **kwargs):

        #code = kwargs['code']
        itineraries = Itinerary.objects.all()
        itineraries_serializer = ItineraryModelSerializer(itineraries, many = True)

        legs = Leg.objects.all()
        legs_serializer = LegModelSerializer(legs, many = True)

        response = {
            'itineraries' : itineraries_serializer.data,
            'legs': legs_serializer.data
        }

        return Response(response)
