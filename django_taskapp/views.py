from django.views.generic import FormView
from django.views.generic import ListView
from .models import ScheduleModel
from .forms import RegistrationForm
from django.contrib import messages
from django.urls import reverse_lazy


class HomeView(ListView):
    template_name = "home.html"
    model = ScheduleModel
    context_object_name = 'schedules'
    ordering = 'date'

class HomePreviousView(ListView):
    template_name = "previous.html"
    model = ScheduleModel
    context_object_name = 'schedules'
    ordering = '-date'


class RegistrationView(FormView):
    template_name = "registration.html"
    form_class = RegistrationForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.save()
        messages.add_message(self.request, messages.SUCCESS, '登録しました！')
        return super().form_valid(form)
