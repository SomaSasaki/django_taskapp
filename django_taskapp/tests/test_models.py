from django_taskapp.models import Schedule
from django.test import TestCase
import datetime
from accounts.models import CustomUser


class TestSchedule(TestCase):
    def setUp(self):
        email = 'test@gmail.com'
        password = 'aaa111'
        user = CustomUser.objects.create_user(email, password)

        summary = "あああ"
        date = datetime.datetime(year=2022, month=12, day=10)
        place = "あいうえお"
        time = datetime.time(hour=23, minute=20)
        detail = "ffweufhweufhwifwekjfwefm,n,emnfwef"
        myTask = Schedule(summary=summary, place=place, date=date, time=time, detail=detail, owner=user)
        myTask.save()

    def test_createTable(self):
        self.assertEqual(Schedule.objects.all().count(), 1)
