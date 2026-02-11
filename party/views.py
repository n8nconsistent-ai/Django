from django.shortcuts import render, redirect
from .models import Customer


def home(request):
    customers = Customer.objects.all().order_by('-id')
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


