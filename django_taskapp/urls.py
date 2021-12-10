from django.urls import path
from django_taskapp.views import HomeView
from django_taskapp.views import HomePreviousView
from django_taskapp.views import RegistrationView
from django_taskapp.views import FriendsView
from django_taskapp.views import Detail

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('previous/', HomePreviousView.as_view(), name='previous'),
    path('register/', RegistrationView.as_view(), name='registration'),
    path('friends/', FriendsView.as_view(), name='friends'),
    path('detail/<int:pk>', Detail.as_view(), name='detail'),
]
