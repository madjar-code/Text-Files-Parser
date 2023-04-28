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

    # class Status(models.TextChoices):
    #     DIRTY = 'dirty', 'dirty'
    #     DURING = 'during', 'during'
    #     READY = 'ready', 'ready'
    
    # status: str = models.CharField(default=Status.DIRTY,
    #                                choices=Status.choices, max_length=255)

    link: str = models.URLField()
    # data: List[NameTimeType] = NameTimeListField()

    class Meta:
        verbose_name = 'Data from One Resume'
        verbose_name_plural = 'Data from Different Resume'

    def __str__(self) -> str:
        return f'{self.link}'


class PositionTime(models.Model):
    resume = models.ForeignKey(
        to=ResumeData, on_delete=models.CASCADE)
    position = models.CharField(max_length=1000)
    time = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'Position Data'
        verbose_name_plural =  'Position Data'
    
    def __str__(self) -> str:
        return f'{self.position} - {self.time}'
    