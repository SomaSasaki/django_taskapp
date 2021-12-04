from django_taskapp.models import Schedule
from django.test import TestCase
import datetime


class TestSchedule(TestCase):
    def setUp(self):
        summary = "あああ"
        date = datetime.datetime(year=2022, month=12, day=10)
        place = "あいうえお"
        time = datetime.time(hour=23, minute=20)
        detail = "ffweufhweufhwifwekjfwefm,n,emnfwef"
        myTask = Schedule(summary=summary, place=place, date=date, time=time, detail=detail)
        myTask.save()

    def test_createTable(self):
        self.assertEqual(Schedule.objects.all().count(), 1)
