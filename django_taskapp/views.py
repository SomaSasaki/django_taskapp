from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic import ListView
from .models import DemoScheduleTable


class HomeView(ListView):
    template_name = "home.html"
    model = DemoScheduleTable
    context_object_name = 'demoSchedule'


class RegistrationTaskView(TemplateView):
    template_name = "taskregister.html"
