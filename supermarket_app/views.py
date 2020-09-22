from django.shortcuts import render
from .models import Customer, Product, Invoice
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import View
from .forms import InvoiceForm

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

def CreateInvoice(request):
    if request.method=='POST':
        invoice_form = InvoiceForm(request.POST)
        if invoice_form.is_valid():
            invoice_form.save()
            return HttpResponseRedirect('/invoices')
    else:
        invoice_form = InvoiceForm()
        context = {'invoice_form':invoice_form}
        return render(request, 'create_invoice.html', context)


class GeneratePdf(View):
    def get(self, request, id, *args, **kwargs):
        invoice = Invoice.objects.get(id = id)
        total_price = 0
        for product in invoice.products.all():
            total_price += product.price
        data = {
            'id': invoice.id,
            'customer_name': invoice.customer_id.name,
            'products': invoice.products,
            # 'price': invoice.product_id.price,
            'total_price':total_price,
            'date':invoice.created_on
        }
        pdf = render_to_pdf('pdf/invoice_pdf.html', data)
        return HttpResponse(pdf, content_type='application/pdf')