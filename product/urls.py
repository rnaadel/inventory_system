from django.urls import path
from . import views

urlpatterns = [
    path('product/', views.productapi.as_view(), name='resource-api'),
]
