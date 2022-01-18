""" Bank models """

# Django
from django.db import models

from flights.models.airline import Airline
#util
from utils.constants_errors import *

class Agent(models.Model):
    """ Agent model """
    name = models.CharField(
        max_length=30,
        null=False,
        unique=False,
        error_messages={
            'required': build_error_message(REQUIRED)
        }
    )
    airline = models.ForeignKey(Airline, on_delete=models.PROTECT)

    def __str__(self):
        """ Return agent """
        return str(self.name)

    REQUIRED_FIELDS = ['name','airline']
