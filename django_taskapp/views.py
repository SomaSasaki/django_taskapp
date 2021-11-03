from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic import ListView
from .models import DemoSchedule

class HomeView(ListView):
	template_name = "home.html"
	model = DemoSchedule
	context_object_name = 'demoSchedule'
