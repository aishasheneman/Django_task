from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import DeliveryOrder
from .forms import DeliveryOrderForm
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import DeliveryOrderSerializer


class DeliveryOrderListView(LoginRequiredMixin, ListView):
    model = DeliveryOrder
    template_name = 'delivery/delivery_list.html'
    context_object_name = 'orders'
    ordering = ['-order_date']

class DeliveryOrderCreateView(LoginRequiredMixin, CreateView):
    model = DeliveryOrder
    form_class = DeliveryOrderForm
    template_name = 'delivery/delivery_form.html'
    success_url = reverse_lazy('delivery_order_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'إضافة طلب توصيل'
        return context

class DeliveryOrderUpdateView(LoginRequiredMixin, UpdateView):
    model = DeliveryOrder
    form_class = DeliveryOrderForm
    template_name = 'delivery/delivery_form.html'
    success_url = reverse_lazy('delivery_order_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'تعديل طلب توصيل'
        return context

class DeliveryOrderDeleteView(LoginRequiredMixin, DeleteView):
    model = DeliveryOrder
    success_url = reverse_lazy('delivery_order_list')
    # نستخدم طريقة POST فقط للحذف لضمان الأمان
    def post(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)


class delivery_api_list (APIView):
    def get (self,request):
        dev1 = DeliveryOrder.objects.all()
        dev2 = DeliveryOrderSerializer(dev1,many = True)
        return Response(dev2.data)


# from django.shortcuts import render, get_object_or_404, redirect
# from django.contrib.auth.decorators import login_required
# from .models import DeliveryOrder
# from .forms import DeliveryOrderForm

# @login_required
# def delivery_order_list(request):
#     orders = DeliveryOrder.objects.all().order_by('-order_date')
#     return render(request, 'delivery/delivery_list.html', {'orders': orders})

# @login_required
# def delivery_create(request):
#     if request.method == 'POST':
#         form = DeliveryOrderForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('delivery_order_list')
#     else:
#         form = DeliveryOrderForm()
#     return render(request, 'delivery/delivery_form.html', {'form': form, 'title': 'إضافة طلب توصيل'})

# @login_required
# def delivery_update(request, pk):
#     order = get_object_or_404(DeliveryOrder, pk=pk)
#     if request.method == 'POST':
#         form = DeliveryOrderForm(request.POST, instance=order)
#         if form.is_valid():
#             form.save()
#             return redirect('delivery_order_list')
#     else:
#         form = DeliveryOrderForm(instance=order)
#     return render(request, 'delivery/delivery_form.html', {'form': form, 'title': 'تعديل طلب توصيل'})

# @login_required
# def delivery_delete(request, pk):
#     order = get_object_or_404(DeliveryOrder, pk=pk)
#     if request.method == 'POST':
#         order.delete()
#     return redirect('delivery_order_list')