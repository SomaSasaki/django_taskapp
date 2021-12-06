from django.views.generic import FormView
from django.views.generic import ListView
from django.views.generic import DetailView
from .models import Schedule
from .forms import RegistrationForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin


class HomeView(LoginRequiredMixin, ListView):
    template_name = "home.html"
    queryset = Schedule.objects.order_by('date')
    context_object_name = 'schedules'

    def get_queryset(self):
        return Schedule.objects.filter(owner=self.request.user)


class HomePreviousView(LoginRequiredMixin, ListView):
    template_name = "previous.html"
    queryset = Schedule.objects.order_by('date')
    context_object_name = 'schedules'

    def get_queryset(self):
        return Schedule.objects.filter(owner=self.request.user)


class RegistrationView(LoginRequiredMixin, FormView):
    template_name = "registration.html"
    form_class = RegistrationForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        form.save()
        return super().form_valid(form)

    def form_invalid(self, form):
        return super().form_invalid(form)


class Detail(LoginRequiredMixin, DetailView):
   model = Schedule
   template_name = 'detail.html'
