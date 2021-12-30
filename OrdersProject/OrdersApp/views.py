from django.shortcuts import render,redirect
from .forms import OrdersModelForm
from .models import Orders
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin

class AddOrdersView(LoginRequiredMixin,View):
    def get(self,request):
        form = OrdersModelForm()
        template_name = 'OrdersApp/addorders.html'
        context = {'form':form}
        return render(request,template_name,context)
    def post(self,request):
        form = OrdersModelForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('show_ord')
        template_name = 'OrdersApp/addorders.html'
        context = {'form':form}
        return render(request,template_name,context)

class ShowOrdersView(View):
    def get(self,request):
        orders = Orders.objects.all()
        template_name = 'OrdersApp/showorders.html'
        context = {'orders':orders}
        return render(request,template_name,context)

class UpdateOrdersView(LoginRequiredMixin,View):
    def get(self,request,i):
        orders = Orders.objects.get(id=i)
        form = OrdersModelForm(instance=orders)
        template_name = 'OrdersApp/addorders.html'
        context = {'form':form}
        return render(request,template_name,context)
    def post(self,request,i):
        orders = Orders.objects.get(id=i)
        form = OrdersModelForm(request.POST,instance=orders)
        if form.is_valid():
            form.save()
            return redirect('show_ord')
        template_name = 'OrdersApp/addorders.html'
        context = {'form':form}
        return render(request,template_name,context)

class DeleteOrdersView(LoginRequiredMixin,View):
    def get(self,request,i):
        orders = Orders.objects.get(id=i)
        template_name = 'OrdersApp/deleteorders.html'
        context = {'orders':orders}
        return render(request,template_name,context)
    def post(self,request,i):
        orders = Orders.objects.get(id=i)
        orders.delete()
        return redirect(request,'show_ord')

class OrdersDetails(View):
    def get(self,request,i):
        orders = Orders.objects.get(id=i)
        template_name = 'OrdersApp/ordersdetail.html'
        context = {'orders':orders}
        return render(request,template_name,context)