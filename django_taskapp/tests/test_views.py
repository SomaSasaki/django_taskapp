from django.test import Client
from django.test import TestCase
from django.urls import reverse_lazy


class TestHomeView(TestCase):
    def test_get_home_view(self):
        c = Client()
        url = reverse_lazy('home')
        response = c.get(url)
        self.assertEqual(response.status_code, 200)
