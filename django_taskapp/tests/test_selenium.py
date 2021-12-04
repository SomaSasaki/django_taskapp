# from django.test import TestCase
# from selenium import webdriver
# import time
# from selenium.webdriver.common.by import By
#
#
# class TestFireFox(TestCase):
#
#     def setUp(self):
#         self.driver = webdriver.Firefox()
#
#     def tearDown(self):
#         self.driver.quit()
#
#     def test_home(self):
#         driver = self.driver
#         driver.get("http://localhost:8000/")
#         self.assertIn("Schedule Viewer", driver.title)
#
#         a_list = []
#         elements = driver.find_elements(By.TAG_NAME, 'a')
#         for e in elements:
#             a_list.append(e.text)
#
#         self.assertIn("HOME", a_list)
#         self.assertIn("SCHEDULE", a_list)
#         self.assertIn("FRIEND", a_list)
#         self.assertIn("Q&A", a_list)
#
#     def test_register(self):
#         driver = self.driver
#         driver.get("http://localhost:8000/register/")
#
#         elements = driver.find_elements(By.TAG_NAME, 'input')
#         elements[1].send_keys('test')
#         elements[2].click()
#         elements[5].submit()
#
#         time.sleep(1)
#
#         cur_url = driver.current_url
#         self.assertEqual(cur_url, "http://localhost:8000/")
