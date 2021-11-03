from django.db import models

class DemoSchedule(models.Model):
    title = models.CharField(max_length=255)
    field = models.CharField(max_length=255)
    date = models.DateTimeField()
    delta = models.IntegerField()
    together = models.CharField(max_length=255)
