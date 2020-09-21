from django.shortcuts import render
from .models import Customer, Product, Invoice
from django.http import HttpResponse
from django.views.generic import View

from .utils import render_to_pdf

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




class GeneratePdf(View):
    def get(self, request, id, *args, **kwargs):
        invoice = Invoice.objects.get(id = id)
        data = {
            'id': invoice.id,
            'customer_name': invoice.customer_id.name,
            'product_name': invoice.product_id.name,
            'price': invoice.product_id.price,
            'date':invoice.created_on
        }
        pdf = render_to_pdf('pdf/invoice_pdf.html', data)
        return HttpResponse(pdf, content_type='application/pdf')