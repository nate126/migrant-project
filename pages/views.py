from django.views.generic import ListView
from .models import *


class HomeView(ListView):
    template_name = "project_content/home.html"
    context_object_name = "mydata"
    model = Locations
    #form_class = EmailForm
    success_url = "/"



