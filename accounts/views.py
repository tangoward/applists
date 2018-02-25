from django.shortcuts import render
from .forms import UserCreateForm
from django.views.generic import CreateView
from django.urls import reverse_lazy
# Create your views here.


class SignUpView(CreateView):
    form_class = UserCreateForm
    template_name = 'accounts/signup.html'
    success_url = reverse_lazy('accounts:login')
