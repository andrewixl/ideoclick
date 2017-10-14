from django.shortcuts import render
from .models import Client

def index(request):
    clients = Client.objects.all().order_by('client_name')
    context = {
        "client" : clients,
    }
    return render(request, 'main/index.html', context)

def team(request):
    return render(request, 'main/team.html')
