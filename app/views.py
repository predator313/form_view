from django.shortcuts import render
from .forms import ContactForm
from django.views.generic.edit import FormView
from django.views.generic.base import TemplateView

# Create your views here.
class ContactFormView(FormView):
    template_name='app/home.html'
    form_class=ContactForm
    success_url='/thanku/'

class Thank(TemplateView):
    template_name='app/thanku.html'
