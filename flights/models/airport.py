""" Airport models """

# Django
from django.db import models

#util
from utils.constants_errors import *

class Airport(models.Model):
    """ Airport model """
    name = models.CharField(
        max_length=30,
        null=False,
        unique=False,
        error_messages={
            'required': build_error_message(REQUIRED),
        }
    )
    code = models.CharField(
        max_length=3,
        null=False,
        unique=True,
        error_messages={
            'required': build_error_message(REQUIRED),
            'unique': build_error_message(UNIQUE)
        }
    )
    def __str__(self):
        """ Return airport """
        return str(self.name)

    REQUIRED_FIELDS = ['name']
