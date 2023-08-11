from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DeleteView, UpdateView, DetailView

from guest.forms import GuestForm, GuestUpdateForm
from guest.models import Guest


# Create your views here.

class GuestCreateView(LoginRequiredMixin,SuccessMessageMixin,CreateView):
    template_name = 'guest/create_guest.html'
    model = Guest
    form_class = GuestForm
    success_url = reverse_lazy('list-guest')
    success_message = 'Congratulations. The guest with the name {t_name} {s_name}  has been created with success.'

    def get_success_message(self, cleaned_data):
        return self.success_message.format(t_name=self.object.first_name, s_name=self.object.last_name)

class GuestListView(LoginRequiredMixin,ListView):
    template_name = 'guest/list_of_guests.html'
    model = Guest
    context_object_name = 'all_guests'


class GuestUpdateView(LoginRequiredMixin,UpdateView):
    template_name = 'guest/update_guest.html'
    model = Guest
    form_class = GuestUpdateForm
    success_url = reverse_lazy('list-guest')

class GuestDeleteView(LoginRequiredMixin,DeleteView):
    template_name = 'guest/delete_guests.html'
    model = Guest
    success_url = reverse_lazy('list-guest')


