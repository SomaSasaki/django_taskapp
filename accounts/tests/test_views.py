#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 31 07:28:38 2021

@author: masahisa
"""

from accounts.models import CustomUser
from django.test import TestCase
from django.urls import reverse
#from django.test import Client

class TestResponse(TestCase):
    def setUp(self):
        email = 'test@gmail.com'
        password = 'aaa111'
        user = CustomUser.objects.create_user(email, password)
        user.save()

        
    def test_login_successful(self):
        logged_in= self.client.login(email='test@gmail.com', password='aaa111')
        self.assertTrue(logged_in)
        self.client.logout()
        
    def test_login_false(self):
        #Not match email
        logged_in= self.client.login(email='gnekrgjn@gmail.com', password='aaa111')
        self.assertFalse(logged_in)
        self.client.logout()
        #uppercase letter for email
        logged_in= self.client.login(email='TEST@gmail.com', password='aaa111')
        self.assertFalse(logged_in)
        self.client.logout()
        #uppercase letter for password
        logged_in= self.client.login(email='test@gmail.com', password='AAA111')
        self.assertFalse(logged_in)
        self.client.logout()
        #Not match password
        logged_in= self.client.login(email='test@gmail.com', password='frewf54')
        self.assertFalse(logged_in)
        self.client.logout()
        
            
    def test_signup_successful(self):
        email_test = 'posttest@gmail.com'
        password_test = 'nlkwwWwer53N'
        
        response = self.client.post('/accounts/signup/',{
            'email':email_test,
            'password1':password_test,
            'password2':password_test
            })

        self.assertRedirects(response,reverse('home'),status_code=302,target_status_code=200)
        #self.assertEquals(response.context['name'],email_test)
        
        logged_in= self.client.login(email=email_test, password=password_test)
        self.assertTrue(logged_in)
        self.client.logout()
        
    def test_signup_false(self):
        #Passwords does not match
        response = self.client.post('/accounts/signup/',{
            'email':'posttest@gmail.com',
            'password1':'nlkwwWwer53N',
            'password2':'rwefy6'
            })
        self.assertEquals(response.status_code,200)
        
        #Password can be guessed
        response = self.client.post('/accounts/signup/',{
            'email':'posttest@gmail.com',
            'password1':'password',
            'password2':'password'
            })
        self.assertEquals(response.status_code,200)
        response = self.client.post('/accounts/signup/',{
            'email':'posttest@gmail.com',
            'password1':'aaa',
            'password2':'aaa'
            })
        self.assertEquals(response.status_code,200)
        
        #Email is not unipue
        response = self.client.post('/accounts/signup/',{
            'email':'test@gmail.com',
            'password1':'ejbfEJhkfe78bDS',
            'password2':'ejbfEJhkfe78bDS'
            })
        self.assertEquals(response.status_code,200)
        
    