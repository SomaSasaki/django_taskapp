#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 18 06:46:53 2021

@author: masahisa
"""

from accounts.models import CustomUser
from django.test import TestCase


class TestCustomUser(TestCase):
    
    def test_base_model(self):
        email = 'test@gmail.com'
        password = 'aaa111'
        user = CustomUser.objects.create_user(email, password)
        self.assertEqual(user.username, 'No Name')
        self.assertEqual(user.email, email)
        self.assertEqual(user.USERNAME_FIELD, 'email')
        self.assertFalse(user.password == password)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)
        self.assertTrue(user.is_active)
        
        user.username = 'testuser'
        user.save()
        self.assertEqual(user.username, 'testuser')
        user.photo = 'test.png'
        user.save()
        self.assertTrue(user.photo)