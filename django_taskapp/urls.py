from django.urls import path
from django_taskapp.views import HomeView

urlpatterns = [
	path('', HomeView.as_view()),
]
