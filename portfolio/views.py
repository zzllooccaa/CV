from django.shortcuts import render
from .models import Project
from .getip import get_client_ip


def home(request):
    projects = Project.objects.all()
    ipaddress = get_client_ip(request)
    adresa = ipaddress
    return render(request, 'portfolio/home.html', {'projects': projects})

