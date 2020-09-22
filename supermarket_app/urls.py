from django.urls import path
from supermarket_app import views
from django.contrib.auth import views as auth_views

urlpatterns =[
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/',auth_views.LogoutView.as_view(), name="logout"),
    path('', views.Home, name='home'),
    path('customers/', views.CustomerList, name='customers'),
    path('products/', views.ProductList, name='products'),
    path('invoices/', views.InvoiceList, name='invoices'),
    path('pdf/<id>', views.GeneratePdf.as_view(), name='invoice_pdf'),



]