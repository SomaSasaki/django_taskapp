from django.urls import path
from django_taskapp.views import HomeView
from django_taskapp.views import HomePreviousView
from django_taskapp.views import RegistrationView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('previous/', HomePreviousView.as_view(), name='previous'),
    path('register/', RegistrationView.as_view(), name='registration'),
]
