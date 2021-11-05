from django.db import models


class DemoScheduleTable(models.Model):
    title = models.CharField(max_length=255)
    field = models.CharField(max_length=255)
    date = models.DateTimeField()
    delta = models.IntegerField(null=True, blank=True)
