from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Product
from .forms import ProductForm

# 1. عرض المنتجات (متاح للجميع)
def product_list(request):
    products = Product.objects.all().order_by('-id')
    
    # حساب الإحصائيات ديناميكياً من قاعدة البيانات
    total_count = products.count()
    total_value = sum(product.price * product.stock for product in products)
    
    context = {
        'products': products,
        'total_count': total_count,
        'total_value': total_value,
    }
    return render(request, 'products/product_list.html', context)

# 2. إضافة منتج جديد (للمسجلين فقط)
def product_create(request):
    if not request.user.is_authenticated:
        messages.error(request, "عذراً، يجب تسجيل الدخول لإضافة منتجات جديدة.")
        return redirect('product_list')
        
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "تم إضافة المنتج الجديد للكتالوج بنجاح!")
            return redirect('product_list')
    else:
        form = ProductForm()
        
    return render(request, 'products/product_form.html', {'form': form, 'title': 'إضافة منتج جديد'})

# 3. تعديل منتج الحالي (للمسجلين فقط)
def product_update(request, pk):
    if not request.user.is_authenticated:
        messages.error(request, "عذراً، لا تمتلك الصلاحية لتعديل المنتجات.")
        return redirect('product_list')
        
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, "تم تحديث بيانات المنتج بنجاح!")
            return redirect('product_list')
    else:
        form = ProductForm(instance=product)
        
    return render(request, 'products/product_form.html', {'form': form, 'title': 'تعديل المنتج الحالي', 'product': product})

# 4. حذف منتج (للمسجلين فقط)
def product_delete(request, pk):
    if not request.user.is_authenticated:
        messages.error(request, "عذراً، لا تمتلك الصلاحية لحذف المنتجات.")
        return redirect('product_list')
        
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        product.delete()
        messages.error(request, "تم حذف المنتج بنجاح من قاعدة البيانات.") # تم إصلاح الدالة هنا من danger إلى error
        return redirect('product_list')
        
    return redirect('product_list')