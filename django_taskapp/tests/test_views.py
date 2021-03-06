from django.test import Client
from django.test import TestCase
from django.urls import reverse_lazy
from django_taskapp.models import Schedule
from accounts.models import CustomUser


class TestHomeView(TestCase):
    def test_get_home_view(self):
        c = Client()
        c.force_login(CustomUser.objects.create_user('tester'))
        response = c.get(reverse_lazy("home"))
        self.assertEqual(response.status_code, 200)


class TestPostSchedule(TestCase):

    def test_status_code(self):
        c = Client()
        c.force_login(CustomUser.objects.create_user('tester'))
        response = c.get(reverse_lazy("registration"))
        self.assertEqual(response.status_code, 200)

    def test_post_registration(self):
        self.assertEqual(Schedule.objects.all().count(), 0)
        c = Client()
        c.force_login(CustomUser.objects.create_user('tester'))
        response = c.post(reverse_lazy("registration"), {
            'summary': 'ใในใ',
            'date': '2021-11-25'
        })
        self.assertRedirects(response, expected_url=reverse_lazy("home"), status_code=302, target_status_code=200)
        self.assertEqual(Schedule.objects.all().count(), 1)
