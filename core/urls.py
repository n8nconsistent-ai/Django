from django.urls import path
from .views import add_customer, home, edit_customer, delete_customer

urlpatterns = [
    path('', home, name='home'),
    path('add-customer/', add_customer, name='add_customer'),
    path('edit-customer/<int:customer_id>/', edit_customer, name='edit_customer'),
    path('delete-customer/<int:customer_id>/', delete_customer, name='delete_customer'),
]
