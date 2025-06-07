from django.views.generic import (
    TemplateView
)
from django.urls import reverse_lazy
from .models import Post

class HomePageView(TemplateView):
    template_name = "pages/home.html"

class AboutPageView(TemplateView):    
    template_name = "pages/about.html"






