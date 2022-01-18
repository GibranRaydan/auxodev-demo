""" Itinerary models """

# Django
from django.db import models
from flights.models.agent import Agent


class Itinerary(models.Model):
    """ Itinerary model """

    agent = models.ForeignKey(Agent, on_delete=models.PROTECT)
    price = models.DecimalField( null=False, default=0.0, max_digits=100, decimal_places=4)
    agent_rating = models.DecimalField( null=False, default=0.0, max_digits=100, decimal_places=4)

    def __str__(self):
        """ Return Itinerary """
        return str(self.agent.name)

    REQUIRED_FIELDS = ['agent','price','agent_rating']
