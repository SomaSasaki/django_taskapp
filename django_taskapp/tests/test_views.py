from django.test import Client
from django.test import TestCase


class TestHomeView(TestCase):
    def test_get_home_view(self):
        c = Client()
        response = c.get('')
        self.assertEqual(response.status_code, 200)
        self.assertTrue('id' in str(response.content))
        self.assertTrue('Title' in str(response.content))
        self.assertTrue('Place' in str(response.content))
        self.assertTrue('Date' in str(response.content))
        self.assertTrue('Countdown' in str(response.content))
