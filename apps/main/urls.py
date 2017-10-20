from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^team$', views.team),
    url(r'^clients$', views.clients),
    url(r'^fulfillment$', views.fulfillment),
    url(r'^subscriptions$', views.subscriptions),
    url(r'^estoremonetization$', views.estoremonetization),
    url(r'^demanddriver$', views.demanddriver),
    url(r'^itemmonitor$', views.itemmonitor),
    url(r'^contentmanagement$', views.contentmanagement),
]
