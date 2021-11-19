from django.test import TestCase
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestFireFox(TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_home(self):
        driver = self.driver
        driver.get("http://localhost:8000")

        ele_text = []
        elements = driver.find_elements(By.TAG_NAME, 'a')
        for e in elements:
            ele_text.append(e.text)

        self.assertIn("Schedule Viewer", driver.title)
        self.assertIn("HOME", ele_text)
        driver.quit()
