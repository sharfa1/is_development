from django.shortcuts import render
from.models import customer
from.forms import Customerform
# Create your views here.
def homepage(request):
    return render(request,template_name='homepage.html')

def home(request):
    return render(request,template_name='about.html')

def customer_view(request):
    if request.method == 'POST':
        customer_form = Customerform(request.POST)
        if customer_form.is_valid():
            customer_form.save()
        else:
            messages.error(request,('your data is invalid try again'))
    customer_form=Customerform()
    return render(request=request,template_name='customer_view.html',context={'customer_form':customer_form})



def customer_list(request):
    customers=customer.objects.all()
    return render(request=request,template_name='customer_list.html',context={'customers':customers})