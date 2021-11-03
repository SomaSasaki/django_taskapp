from django.db import models
import datetime

class DemoSchedule(models.Model):
    title = models.CharField(max_length=255)
    field = models.CharField(max_length=255)
    date = models.DateTimeField()
    delta = models.IntegerField()
    together = models.CharField(max_length=255)

# demo = DemoSchedule(title='か', field='き', \
#                     date=datetime.datetime(year=2022, month=2, day=1, hour=12), \
#                     delta=2, together="けんじ")
# demo.save()
