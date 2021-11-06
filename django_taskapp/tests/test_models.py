from django_taskapp.models import ScheduleModel
from django.test import TestCase
import datetime


class TestScheduleModel(TestCase):
    def setUp(self):
        summary = "あああ"
        place = "あいうえお"
        date = datetime.datetime(year=2022, month=12, day=10)
        time = datetime.time(hour=23, minute=20)
        myTask = ScheduleModel(summary=summary, place=place, date=date, time=time)
        myTask.save()

    def test_createTable(self):
        self.assertEqual(ScheduleModel.objects.all().count(), 1)
