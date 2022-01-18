""" Airline models """

# Django
from django.db import models

#util
from utils.constants_errors import *

class Airline(models.Model):
    """ Airline model """
    name = models.CharField(
        max_length=30,
        null=False,
        unique=True,
        error_messages={
            'required': build_error_message(EXIST),
            'unique': build_error_message(UNIQUE)
        }
    )
    def __str__(self):
        """ Return airline """
        return str(self.name)

    REQUIRED_FIELDS = ['name']
