from django.urls import path
from .views import home, add_customer

urlpatterns = [
    path('', home, name='home'),
    path('add/', add_customer, name='add_customer'),
]
