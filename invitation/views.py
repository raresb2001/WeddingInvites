from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import request
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView

from invitation.forms import InvitationForm, InvitationUpdateForm
from invitation.models import Invitation


# TemplateView -> este o clasa de baza generica care poate fi utilizata pentru a afisa o pagina html intr-o aplicatie web


class InvitationCreateView(LoginRequiredMixin,SuccessMessageMixin,CreateView):
    template_name = 'invitation/create_invitation.html'  # calea catre fisierul html unde va fi generat formularul
    model = Invitation  # formularul din html se va genera pe baza modelului(clasa din models.py)
    form_class = InvitationForm  # definim campurile din formualr, pe care le dorim
    success_url = reverse_lazy('list-invitation')  # dupa ce dom accesa butonul de save, utilizatorul va fi redirectionat pe pagina mentionat
    success_message = 'Congratulations. The invitation with the name  {f_title}  has been created with  success.'

    def get_success_message(self, cleaned_data):
        return self.success_message.format(f_title=self.object.title)


class InvitationListView(LoginRequiredMixin,ListView):
    template_name = 'invitation/list_of_invitations.html'
    model = Invitation
    context_object_name = 'all_invitation'


class InvitationUpdateView(LoginRequiredMixin,UpdateView):
    template_name = 'invitation/update_invitation.html'
    model = Invitation
    form_class = InvitationUpdateForm
    success_url = reverse_lazy('list-invitation')

class InvitationDeleteView(LoginRequiredMixin,DeleteView):
    template_name = 'invitation/delete_invitation.html'
    model = Invitation
    success_url = reverse_lazy('list-invitation')


class InvitationDetailView(DetailView):
    template_name = 'invitation/details_invitation.html'
    model = Invitation