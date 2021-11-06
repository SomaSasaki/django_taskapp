from django.db import models
import datetime


class ScheduleModel(models.Model):
    summary = models.CharField(max_length=20)
    place = models.CharField(max_length=20)
    date = models.DateField(default=datetime.date.today())
    time = models.TimeField(default=datetime.time(hour=12, minute=0))
    detail = models.TextField(blank=True)
    author = models.CharField(max_length=20, default="あなた")
