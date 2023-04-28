from django.db import models


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
    # data: List[NameTimeType] = NameTimeListField()
    number: str = models.PositiveBigIntegerField(
        blank=True, null=True)
    link: str = models.URLField()
    class Meta:
        verbose_name = 'Data from One Resume'
        verbose_name_plural = 'Data from Different Resume'

    def __str__(self) -> str:
        return f'{self.id}'


class PositionTime(models.Model):
    resume = models.ForeignKey(
        to=ResumeData, on_delete=models.CASCADE)
    local_order = models.PositiveSmallIntegerField()
    position = models.CharField(max_length=1000)
    time = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'Position Data'
        verbose_name_plural = 'Position Data'

    def __str__(self) -> str:
        return f'{self.position} - {self.time}'
