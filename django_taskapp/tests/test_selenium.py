from django.test import TestCase
from selenium import webdriver


class TestMySelenium(TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_home(self):
        driver = self.driver
        driver.get("http://localhost:8000")
        self.assertIn("Schedule Viewer", driver.title)
