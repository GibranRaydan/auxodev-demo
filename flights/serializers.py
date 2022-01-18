"""serializers """

# Django REST Framework
from rest_framework import serializers
# Models
from flights.models import Itinerary, Leg 

class LegModelSerializer(serializers.ModelSerializer):
    """ Leg model serializers """
    arrival_airport = serializers.SlugRelatedField(
        many = False, read_only = True, slug_field='code'
    )
    departure_airport = serializers.SlugRelatedField(
        many = False, read_only = True, slug_field='code'
    )
    airline_name = serializers.StringRelatedField(many=False,read_only=True, source = 'airline')
    airline_id = serializers.PrimaryKeyRelatedField(many=False, read_only=True, source = 'airline')


    class Meta:
        model = Leg
        fields = ('id','stops','duration','arrival_airport','departure_airport','airline_id','airline_name')


class ItineraryModelSerializer(serializers.ModelSerializer):
    """ Itinerary model serializers """
    class Meta:
        model = Itinerary
        fields = ('id','legs','price','agent_rating')

