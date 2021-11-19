from django.test import Client
from django.test import TestCase
from django.urls import reverse_lazy
from django_taskapp.models import ScheduleModel


class TestHomeView(TestCase):
    def test_get_home_view(self):
        c = Client()
        response = c.get(reverse_lazy('home'))
        self.assertEqual(response.status_code, 200)


class TestPostSchedule(TestCase):
    def test_status_code(self):
        c = Client()
        response = c.get(reverse_lazy("registration"))
        self.assertEqual(response.status_code, 200)

    def test_post_registration(self):
        self.assertEqual(ScheduleModel.objects.all().count(), 0)
        c = Client()
        response = c.post(reverse_lazy("registration"), {
            'summary': 'テスト',
            'date': '2021-11-25'
        })
        self.assertRedirects(response, expected_url=reverse_lazy("home"), status_code=302, target_status_code=200)
        self.assertEqual(ScheduleModel.objects.all().count(), 1)
