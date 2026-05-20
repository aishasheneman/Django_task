from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import DeliveryOrder
from .forms import DeliveryOrderForm

@login_required
def delivery_order_list(request):
    orders = DeliveryOrder.objects.all().order_by('-order_date')
    return render(request, 'delivery/delivery_list.html', {'orders': orders})

@login_required
def delivery_create(request):
    if request.method == 'POST':
        form = DeliveryOrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('delivery_order_list')
    else:
        form = DeliveryOrderForm()
    return render(request, 'delivery/delivery_form.html', {'form': form, 'title': 'إضافة طلب توصيل'})

@login_required
def delivery_update(request, pk):
    order = get_object_or_404(DeliveryOrder, pk=pk)
    if request.method == 'POST':
        form = DeliveryOrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('delivery_order_list')
    else:
        form = DeliveryOrderForm(instance=order)
    return render(request, 'delivery/delivery_form.html', {'form': form, 'title': 'تعديل طلب توصيل'})

@login_required
def delivery_delete(request, pk):
    order = get_object_or_404(DeliveryOrder, pk=pk)
    if request.method == 'POST':
        order.delete()
    return redirect('delivery_order_list')