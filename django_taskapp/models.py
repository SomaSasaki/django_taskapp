from django.db import models
import datetime


class DemoScheduleTable(models.Model):
    title = models.CharField(max_length=255)
    field = models.CharField(max_length=255)
    date = models.DateTimeField()
    delta = models.IntegerField()


# demo = DemoScheduleTable(title='クラス会', field='お台場', \
#                          date=datetime.datetime(year=2022, month=12, day=10, hour=12), \
#                          delta=4)
# demo.save()
