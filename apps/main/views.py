from django.shortcuts import render
from .models import Client, Employee

def index(request):
    clients = Client.objects.filter(client_type = 'large').all().order_by('client_name')
    context = {
        "client" : clients,
    }
    return render(request, 'main/index.html', context)

def team(request):
    operations = Employee.objects.filter(employee_type = "operations").all()
    catalog = Employee.objects.filter(employee_type = "catalog").all()
    account_management = Employee.objects.filter(employee_type = "account_management").all()
    development = Employee.objects.filter(employee_type = "development").all()
    marketing = Employee.objects.filter(employee_type = "marketing").all()
    support = Employee.objects.filter(employee_type = "support").all()
    context = {
        "operations" : operations,
        "catalog" : catalog,
        "account_management" : account_management,
        "development" : development,
        "marketing" : marketing,
        "support" : support,
    }
    return render(request, 'main/team.html', context)

def clients(request):
    clients = Client.objects.all().order_by('client_name')
    context = {
        "client" : clients,
    }
    return render(request, 'main/client.html', context)

def fulfillment(request):
    return render(request, 'main/services/fulfillment.html')

def marketing(request):
    return render(request, 'main/services/marketing.html')

def consulting(request):
    return render(request, 'main/services/consulting.html')

def demanddriver(request):
    return render(request, 'main/services/demanddriver.html')

def itemmonitor(request):
    return render(request, 'main/services/itemmonitor.html')

def contentdevelopment(request):
    return render(request, 'main/services/contentdevelopment.html')
