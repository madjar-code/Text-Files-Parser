from typing import Optional, List
from django.db import models
from .types import *


class NameTimeListField(models.TextField):
    def get_prep_value(self, value: Optional[str]
                       ) -> Optional[str]:
        if not value:
            return None
        return value

    def to_python(self, value: Optional[str]
                  ) -> Optional(List[NameTimeType]):
        if not value:
            return None
        return value.split('), ')
