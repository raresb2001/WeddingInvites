from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.utils.datetime_safe import datetime
from django.views.generic import CreateView

from userextend.forms import UserForm
from userextend.models import History


# Create your views here.

class UserCreateView(CreateView):
    template_name = 'userextend/create_user.html'
    model = User
    form_class = UserForm
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        if form.is_valid():
            new_user = form.save(commit=False)  # oprim salvarea datelor pentru ca urmeaza sa le modificam
            subject = 'Cont nou in aplicatie!'
            message = f"Felicitari. Ai un cont nou in aplicatie. Username este: {new_user.username}"
            new_user.save()

            message = (f"first_name: {new_user.first_name}, last_name {new_user.last_name}",
                       f"email: {new_user.email}, username: {new_user.username}")

            user = new_user.id
            created_at = datetime.now()
            History.objects.create(message=message, user_id=user, created_at=created_at)

        return redirect('login')