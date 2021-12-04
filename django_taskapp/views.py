from django.views.generic import FormView
from django.views.generic import ListView
from .models import Schedule
from .forms import RegistrationForm
from django.contrib import messages
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin


class HomeView(LoginRequiredMixin, ListView):
    template_name = "home.html"
    queryset = Schedule.objects.order_by('date')
    context_object_name = 'schedules'


class HomePreviousView(LoginRequiredMixin, ListView):
    template_name = "previous.html"
    queryset = Schedule.objects.order_by('date')
    context_object_name = 'schedules'


class RegistrationView(LoginRequiredMixin, FormView):
    template_name = "registration.html"
    form_class = RegistrationForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.save()
        # messages.add_message(self.request, messages.SUCCESS, '登録しました！')
        return super().form_valid(form)

    def form_invalid(self, form):
        # messages.error(self.request, '入力内容をご確認ください。')
        return super().form_invalid(form)
