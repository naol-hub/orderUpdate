from django.shortcuts import render , redirect
from .models import *
from .forms import OrderForm, createUerForm
from  django.forms import inlineformset_factory

from django.contrib.auth.forms import UserCreationForm
from .filters import OrderFilter

# Create your views here.
def home(request):
    customer = Customer.objects.all()
    orders = Order.objects.all()
    
    total_order = customer.count()
    total_pending =orders.filter(status = 'pending').count() 
    ## in other form you can in other
    total_deliver =Order.objects.filter(status = 'Out For Delivery').count()
    context ={'customer': customer , 'orders': orders , 'total_deliver': total_deliver ,'total_pending' :total_pending, 'total_order': total_order}


    return render(request,'accounts/dashboard.html', context)

def products(request):
    Product_vir = Product.objects.all()
    context ={'pass_varible': Product_vir}
    return render(request,'accounts/product.html', context)    
def customer(request, pk):
    customer = Customer.objects.get(id = pk)
    orders = customer.order_set.all ()
    order_counts = orders.count()
    myFilter = OrderFilter(request.GET , queryset=orders)
    orders = myFilter.qs

    context = {'customer':customer, 'orders':orders,'order_counts':order_counts, 'myFilter':myFilter,}


    return render(request,'accounts/customer.html',context)  

def createOrder(request, pk):
    custom = Customer.objects.get(id = pk)
    #form = OrderForm(initial={'customer':custom})
    form_variable = inlineformset_factory(Customer , Order, fields=('product','status'), extra=6)

    formV =  form_variable( queryset= Order.objects.none(), instance=custom)
    if request.method=='POST':
        #print('The printing:', request.POST)
        #form = OrderForm(request.POST)
        formV = form_variable(request.POST , instance=custom)
        if formV.is_valid():
            formV.save()
            return redirect('/')



    context ={'formVariable':formV}
    return render(request, 'accounts/order_form.html', context)


def updateOrder(request, pk):
    order = Order.objects.get(id=pk)
    form = OrderForm(instance=order)
    if request.method=='POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('/')

    context ={'form':form}
    return render(request, 'accounts/order_form.html', context)

def deleteOrder(request , pk ):
    order = Order.objects.get(id=pk)
    if request.method == 'POST':
        order.delete()
        return redirect('/')
    context ={'item': order}

    return render(request, 'accounts/delete.html', context)

def registerpage(request):
    form =createUerForm()
    if request.method =='POST':
        form = createUerForm(request.POST)
        if form.is_valid():
            form.save()

    context ={'form':form }
    
    return render(request, 'accounts/register.html', context)
       
def loginpage(request):
    return render (request ,'accounts/login.html')