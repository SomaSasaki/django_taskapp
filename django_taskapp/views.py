from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic import ListView
from .models import DemoModel

class HomeView(ListView):
	template_name = "home.html"
	model = DemoModel
	context_object_name = 'demomodels'
