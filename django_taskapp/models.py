from django.db import models
import datetime

class DemoSchedule(models.Model):
    title = models.CharField(max_length=255)
    field = models.CharField(max_length=255)
    date = models.DateTimeField()
    delta = models.IntegerField()
    together = models.CharField(max_length=255)
# demo = DemoSchedule(title='あいうえおかきくけこさしすせそたちつてと', field='お台場', \
#                     date=datetime.datetime(year=2022, month=12, day=10, hour=12), \
#                     delta=4, together="けんじ,ささき,たろう")
# demo.save()
