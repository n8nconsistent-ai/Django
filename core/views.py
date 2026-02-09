from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from .models import Customer
from django.core.paginator import Paginator


def home(request):
    customers = Customer.objects.all()

    # filters
    name = request.GET.get('name', '')
    email = request.GET.get('email', '')
    phone = request.GET.get('phone', '')
    country = request.GET.get('country', '')

    if name:
        customers = customers.filter(name__icontains=name)
    if email:
        customers = customers.filter(email__icontains=email)
    if phone:
        customers = customers.filter(phone__icontains=phone)
    if country:
        customers = customers.filter(country__icontains=country)

    # ✅ FIXED ORDER
    customers = customers.order_by('-updated_at', '-id')

    # pagination
    per_page = int(request.GET.get('per_page', 10))
    paginator = Paginator(customers, per_page)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'customers': page_obj,
        'page_obj': page_obj,
        'per_page': per_page,
        'filters': {
            'name': name,
            'email': email,
            'phone': phone,
            'country': country,
        }
    }

    return render(request, 'core/home.html', context)


def add_customer(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        country = request.POST.get('country')

        Customer.objects.create(
            name=name,
            email=email,
            phone=phone,
            country=country
        )

        return redirect('home')

    return render(request, 'add_customer.html')

def edit_customer(request, customer_id):
    customer = get_object_or_404(Customer, id=customer_id)
    
    if request.method == "POST":
        customer.name = request.POST.get('name')
        customer.email = request.POST.get('email')
        customer.phone = request.POST.get('phone')
        customer.country = request.POST.get('country')
        customer.save()
        return redirect('home')
    
    return render(request, 'edit_customer.html', {'customer': customer})

def delete_customer(request, customer_id):
    customer = get_object_or_404(Customer, id=customer_id)
    customer.delete()
    return redirect('home')
