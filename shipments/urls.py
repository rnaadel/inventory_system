from django.urls import path
from . import views

urlpatterns = [
    path('shipments/', views.shipmentapi.as_view(), name='resource-api'),
]
