# Datetime
from datetime import date

# Models
from flights.models import *

def create_airport(name='test_airport', code='MGT'):
    airport = Airport.objects.create(name=name, code=code)
    return airport

def create_airline(name='test_airline'):
    airline = Airline.objects.create(name=name)
    return airline

def create_agent(name='test_agent',airline=None):
    if airline == None:
        airline = create_airline()
    agent = Agent.objects.create(name=name,airline=airline)
    return agent

def create_itinerary(name='test_itinerary1',agent=None,price=1000,agent_rating=10):
    if agent == None:
        agent = create_agent()
    itinerary = Itinerary.objects.create(
        price=price,agent=agent,agent_rating=agent_rating
        )
    return itinerary

def create_leg(
    departure_airport=None,
    arrival_airport=None,
    itinerary=None,
    departure_time=date.today(),
    arrival_time=date.today(),
    airline=None,duration=60,
    stops=0):
    if departure_airport == None:
        departure_airport = create_airport(name='departure')
    if arrival_airport == None:
        arrival_airport = create_airport(name='arrival')
    if airline == None:
        airline = create_airline('airline_test')
    if itinerary == None:
        agent = create_agent(name='agent_name', airline=airline)
        itinerary = create_itinerary(name='test_itinerary', agent=agent)

    leg = Leg.objects.create(
        departure_airport=departure_airport,
        arrival_airport=arrival_airport,
        departure_time=departure_time,
        arrival_time=arrival_time,
        airline=airline,
        itinerary=itinerary,
        stops=stops
        )
    return leg