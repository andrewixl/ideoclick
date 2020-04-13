from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^team$', views.team),
    url(r'^clients$', views.clients),
    url(r'^fulfillment$', views.fulfillment),
    url(r'^marketing$', views.marketing),
    url(r'^consulting$', views.consulting),
    url(r'^demanddriver$', views.demanddriver),
    url(r'^itemmonitor$', views.itemmonitor),
    url(r'^contentdevelopment$', views.contentdevelopment),
    url(r'^press$', views.press),
    url(r'^quote$', views.quote),
]
