""" Bank models admin """

# Django
from django.contrib import admin

# Models
from flights.models import *

@admin.register(Airport)
class AirportAdmin(admin.ModelAdmin):
    """ Airport model admin """
    # list_display = '__all__'
    # search_fields = ('name', 'code',)
    # list_filter = ('is_active', 'name', 'code',)

@admin.register(Airline)
class AirlineAdmin(admin.ModelAdmin):
    """ Airline model admin """
    # list_display = '__all__'
    # search_fields = ('name', 'code',)
    # list_filter = ('is_active', 'name', 'code',)

@admin.register(Leg)
class LegAdmin(admin.ModelAdmin):
    """ Leg model admin """
    # list_display = '__all__'
    # search_fields = ('name', 'code',)
    # list_filter = ('is_active', 'name', 'code',)

@admin.register(Agent)
class AgentAdmin(admin.ModelAdmin):
    """ agent model admin """
    # list_display = '__all__'
    # search_fields = ('name', 'code',)
    # list_filter = ('is_active', 'name', 'code',)

@admin.register(Itinerary)
class ItineraryAdmin(admin.ModelAdmin):
    """ Itinerary model admin """
    list_display = ('id','price','agent_rating')
    search_fields = ('id', 'price','agent_rating')
    list_filter = ('price','agent_rating')




