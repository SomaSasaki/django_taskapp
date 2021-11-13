from django.test import Client
from django.test import TestCase
from django.urls import reverse_lazy
from django_taskapp.models import ScheduleModel


class TestPostValidateSchedule(TestCase):
    def test_post_registration(self):
        self.assertEqual(ScheduleModel.objects.all().count(), 0)
        c = Client()
        # False Over 20character
        response = c.post(reverse_lazy("registration"), {
            'summary': '123456789012345678901',
            'date': '2021-11-25'
        })
        self.assertEqual(response.status_code, 200)
        self.assertEqual(ScheduleModel.objects.all().count(), 0)
        # Clear symbols
        response = c.post(reverse_lazy("registration"), {
            'summary': '!"#$%&()-=^~¥|[{@`:*',
            'date': '2021-11-25'
        })
        self.assertRedirects(response, expected_url=reverse_lazy("home"), status_code=302, target_status_code=200)
        self.assertEqual(ScheduleModel.objects.all().count(), 1)
        # Clear symbols
        response = c.post(reverse_lazy("registration"), {
            'summary': ';+]}_/?.>,<',
            'date': '2021-11-25'
        })
        self.assertRedirects(response, expected_url=reverse_lazy("home"), status_code=302, target_status_code=200)
        self.assertEqual(ScheduleModel.objects.all().count(), 2)
        # Clear PNG
        response = c.post(reverse_lazy("registration"), {
            'summary': 'sample.png',
            'date': '2021-11-25'
        })
        self.assertRedirects(response, expected_url=reverse_lazy("home"), status_code=302, target_status_code=200)
        self.assertEqual(ScheduleModel.objects.all().count(), 3)
        # Clear SQL
        response = c.post(reverse_lazy("registration"), {
            'summary': "'1' or '1' = '1';--",
            'date': '2021-11-25'
        })
        self.assertRedirects(response, expected_url=reverse_lazy("home"), status_code=302, target_status_code=200)
        self.assertEqual(ScheduleModel.objects.all().count(), 4)


