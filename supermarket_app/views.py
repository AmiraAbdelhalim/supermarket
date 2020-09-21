from django.shortcuts import render
from .models import Customer, Product, Invoice

# Create your views here
def Home(request):
    return render(request, 'home.html')

def CustomerList(request):
    customers = Customer.objects.all()
    return render(request, 'customer.html', {'customers': customers})

def ProductList(request):
    products = Product.objects.all()
    return render(request, 'product.html', {'products': products})

def InvoiceList(request):
    invoices = Invoice.objects.all()
    context = {
        'invoices': invoices,
    }
    return render(request, 'invoice.html', context)