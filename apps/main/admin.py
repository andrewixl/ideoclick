from django.contrib import admin
from .models import Client, Employee
# Register your models here.

class EmployeeAdmin(admin.ModelAdmin):
    list_filter = ('employee_type',)
admin.site.register(Employee, EmployeeAdmin)

class ClientAdmin(admin.ModelAdmin):
    list_filter = ('client_type',)
admin.site.register(Client, ClientAdmin)
