from django.shortcuts import render
from django.views.generic import FormView

from home.forms import RegistrationForm


class HomeView(FormView):
    form_class = RegistrationForm
    template_name = "home/home.html"
