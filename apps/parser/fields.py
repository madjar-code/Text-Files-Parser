
from django.db import models
from .types import *


SEPARATOR = ';'


class NameTimeListField(models.TextField):
    description = 'Stores a python list'

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def from_db_to_value(self, value, expression, connection):
        if not value:
            return value
        if isinstance(value, str):
            return value.split(SEPARATOR)

    def to_python(self, value):
        if not value:
            value = []
        if isinstance(value, list):
            return value
        if isinstance(value, str):
            return value.split(SEPARATOR)

    def get_prep_value(self, value):
        if not value:
            return None
        if isinstance(value, str):
            return value
        if isinstance(value, list):
            return SEPARATOR.join(value)

    def value_to_string(self, obj):
        value = self.value_from_object(obj)
        return self.get_prep_value(value)
