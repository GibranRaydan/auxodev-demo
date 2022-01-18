# Django REST Framework
from rest_framework import status


class Errors():
    def __init__(
        self,
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        error_code=0,
        error_mensage='A server error occurred.'
    ):
        self.status_code = status_code
        self.error_mensage = error_mensage
        self.error_code = error_code


def build_error_message(error):
    return f"error_message : {str(error.error_mensage)}, error_code : {error.error_code}"


DEFAULD = Errors()

EXIST = Errors(
    status_code=status.HTTP_400_BAD_REQUEST,
    error_code=1,
    error_mensage='This already exists.'
)

UNIQUE = Errors(
    status_code=status.HTTP_400_BAD_REQUEST,
    error_code=2,
    error_mensage='This must be unique.'
)

REQUIRED = Errors(
    status_code=status.HTTP_400_BAD_REQUEST,
    error_code=3,
    error_mensage='This is required.'
)
