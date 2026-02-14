from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add/', views.add_customer, name='add_customer'),
    path('edit/<int:id>/', views.edit_customer, name='edit_customer'),
    path('delete/<int:id>/', views.hard_delete_customer, name='hard_delete_customer'),
    path('disable/<int:id>/', views.disable_customer, name='disable_customer'),

]
