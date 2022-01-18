""" Itinerary models """

# Django
from django.db import models
# Models
from flights.models.agent import Agent
# Utils
from utils.constants_errors import *



class Itinerary(models.Model):
    """ Itinerary model """
    name = models.CharField(
        max_length=30,
        null=False,
        unique=False,
        error_messages={
            'required': build_error_message(EXIST),
        }
    )

    agent = models.ForeignKey(Agent, on_delete=models.PROTECT)
    price = models.DecimalField( null=False, default=0.0, max_digits=100, decimal_places=4)
    agent_rating = models.DecimalField( null=False, default=0.0, max_digits=10, decimal_places=2)

    def __str__(self):
        """ Return Itinerary """
        return str(self.name)

    REQUIRED_FIELDS = ['agent','price','agent_rating']
