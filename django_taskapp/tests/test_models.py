from django_taskapp.models import DemoScheduleTable
from django.test import TestCase
import datetime


class TestDemoScheduleTable(TestCase):
    def setUp(self):
        title = "あああ"
        field = "あいうえお"
        date = datetime.datetime(year=2022, month=12, day=10, hour=12)
        delta = 4
        myTask = DemoScheduleTable(title, field, date, delta)
        myTask.save()

    def test_createTable(self):
        title = "あああ"
        field = "あいうえお"
        date = datetime.datetime(year=2022, month=12, day=10, hour=12)
        delta = 4
        self.assertEqual(DemoScheduleTable.objects.all().count(), 1)
        self.assertEqual(DemoScheduleTable.title, title)
        self.assertEqual(DemoScheduleTable.field, field)
        self.assertEqual(DemoScheduleTable.date, date)
        self.assertEqual(DemoScheduleTable.delta, delta)
