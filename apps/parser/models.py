from typing import List
from django.db import models
from .fields import NameTimeListField
from .types import NameTimeType


class ResumeData(models.Model):     
    # STATUS_DIRTY = 'dirty'
    # STATUS_DURING = 'during'
    # STATUS_READY = 'ready'

    # STATUS_CHOICES = (
    #     (STATUS_DIRTY, 'dirty'),
    #     (STATUS_DURING, 'during'),
    #     (STATUS_READY, 'ready'),
    # )

    class Status(models.TextChoices):
        STATUS_DIRTY = 'dirty'
        STATUS_DURING = 'during'
        STATUS_READY = 'ready'

        DIRTY = STATUS_DIRTY, 'dirty'
        DURING = STATUS_DURING, 'during'
        READY = STATUS_READY, 'ready'

    link: str = models.URLField()
    status: str = models.CharField(default=Status.DIRTY,
                                   choices=Status.choices, max_length=255)
    data: List[NameTimeType] = NameTimeListField()

    class Meta:
        verbose_name = 'Data from One Resume'
        verbose_name_plural = 'Data from Different Resume'
