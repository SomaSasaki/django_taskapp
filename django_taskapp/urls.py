from django.urls import path
from django_taskapp.views import HomeView
from django_taskapp.views import RegistrationTaskView

urlpatterns = [
    path('', HomeView.as_view()),
    path('register/', RegistrationTaskView.as_view()),
]
