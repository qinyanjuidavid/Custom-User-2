from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from accounts.forms import SupplierSignupForm,CustomerSignupForm
from django.views.generic import CreateView
from accounts.models import User
from django.contrib.auth import login
from accounts.decorators import supplier_required,customer_required


def Home(request):
    context={

    }
    return render(request,'accounts/home.html',context)

class SupplierSignupView(CreateView):
    model=User
    form_class=SupplierSignupForm
    template_name='accounts/supplier.html'
    def get_context_data(self,**kwargs):
        kwargs['user_type']='supplier'
        return super().get_context_data(**kwargs)
    def form_valid(self,form):
        if form.is_valid():
            user=form.save()
            login(self.request,user)
            return HttpResponseRedirect('/login/')
class CustomerSignupView(CreateView):
    model=User
    form_class=CustomerSignupForm
    template_name='accounts/customer.html'
    def get_context_data(self,**kwargs):
        kwargs['user_type']='customer'
        return super().get_context_data(**kwargs)
    def form_valid(self,form):
        if form.is_valid():
            user=form.save()
            login(self.request,user)
            return HttpResponseRedirect('/login/')
