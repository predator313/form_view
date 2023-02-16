from django.shortcuts import render
from .forms import ContactForm
from django.views.generic.edit import FormView

# Create your views here.
class ContactFormView(FormView):
    template_name='app/home.html'
    form_class=ContactForm
