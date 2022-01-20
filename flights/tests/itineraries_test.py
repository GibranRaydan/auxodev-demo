""" Itineraries test !"""
# Django Rest Framework
from rest_framework.test import APITestCase
from rest_framework.test import APIClient
from rest_framework import status
# test setup
from flights.tests.setup import * 

# pip install pytest
# pip install pytest-django

URL = '/flights/itineraries/'


class ItinerariesTest(APITestCase):
    def setUp(self):
        self.airport_test = create_airport(name='test_airport1', code='ABC')
        self.airline_test = create_airline(name='test_airline1')
        self.agent_test = create_agent(name='test_agent1',airline=self.airline_test)
        self.itinerary_test = create_itinerary(agent=self.agent_test,price=10000,agent_rating=9.1)
        self.leg_test = create_leg(
            arrival_airport=self.airport_test,
            airline=self.airline_test,
            itinerary=self.itinerary_test)

    def test_create_airport(self):
        airport = Airport.objects.get(name='test_airport1',code='ABC')
        self.assertEqual(airport.code, self.airport_test.code)

    def test_create_airport(self):
        airline = Airline.objects.get(name='test_airline1')
        self.assertEqual(airline.name, self.airline_test.name)

    def test_create_agent(self):
        agent = Agent.objects.get(name='test_agent1',airline=self.airline_test)
        self.assertEqual(agent.name, self.agent_test.name)
    
    def test_create_itinerary(self):
        itinerary = Itinerary.objects.get(agent=self.agent_test,price=10000)
        self.assertEqual(itinerary.agent, self.agent_test)

    def test_create_itinerary(self):
        leg = Leg.objects.get(airline=self.airline_test, arrival_airport= self.airport_test)
        self.assertEqual(leg.airline, self.airline_test)

    def test_get_itineraries(self):
        example_body = {
            "itineraries": [
                {
                    "id": 1,
                    "legs": [1],
                "price": "10000.0000",
                "agent_rating": "9.10"
                }
            ],
            "legs": [
                {
                    "id": 1,
                    "stops": 0,
                    "duration": 60,
                    "arrival_airport": "ABC",
                    "departure_airport": "MGT",
                    "airline_id": 1,
                    "airline_name": "test_airline1",
                    "departure_time": "2022-01-20T00:00:00Z",
                    "arrival_time": "2022-01-20T00:00:00Z"
                }
            ]
        }
        client = APIClient()
        response = client.get(path=URL, format='json')
        self.assertEqual(response.status_code,200)
        self.assertEqual(response.data,example_body)


    


        