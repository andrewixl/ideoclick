from django.shortcuts import render
from .models import Client

def index(request):
    clients = Client.objects.all().order_by('client_name')[:14]
    context = {
        "client" : clients,
    }
    return render(request, 'main/index.html', context)

def team(request):
    return render(request, 'main/team.html')

def clients(request):
    clients = Client.objects.all().order_by('client_name')
    context = {
        "client" : clients,
    }
    return render(request, 'main/client.html', context)

def fulfillment(request):
    return render(request, 'main/services/fulfillment.html')

def subscriptions(request):
    return render(request, 'main/services/subscriptions.html')

def estoremonetization(request):
    return render(request, 'main/services/estoremonetization.html')

def demanddriver(request):
    return render(request, 'main/services/demanddriver.html')

def itemmonitor(request):
    return render(request, 'main/services/itemmonitor.html')

def contentmanagement(request):
    return render(request, 'main/services/contentmanagement.html')
