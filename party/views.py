from django.shortcuts import render, redirect
from .models import Customer


def home(request):
    customers = Customer.objects.filter(is_deleted=False)
    return render(request, 'party/home.html', {'customers': customers})



def add_customer(request):

    if request.method == "POST":
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        country = request.POST.get('country')
        
        customer_type = request.POST.get('customer_type')
        interested_items = request.POST.getlist('interested_items')

        Customer.objects.create(
            name=name,
            phone=phone,
            email=email,
            country=country,
            customer_type=customer_type,
            interested_items=interested_items
        )

        return redirect('home')

    return render(request, 'party/add_customer.html')

from django.shortcuts import render, redirect, get_object_or_404
from .models import Customer


def edit_customer(request, id):
    customer = get_object_or_404(Customer, id=id)

    if request.method == "POST":
        customer.name = request.POST.get('name')
        customer.email = request.POST.get('email')
        customer.phone = request.POST.get('phone')
        customer.country = request.POST.get('country')
        customer.customer_type = request.POST.get('customer_type')
        customer.interested_items = request.POST.getlist('interested_items')

        customer.save()
        return redirect('home')

    return render(request, 'party/edit_customer.html', {'customer': customer})

def hard_delete_customer(request, id):
    customer = get_object_or_404(Customer, id=id)
    customer.delete()
    return redirect('home')

def disable_customer(request, id):
    customer = get_object_or_404(Customer, id=id)
    customer.is_deleted = True
    customer.save()
    return redirect('home')

    customer.delete()
    return redirect('home')


