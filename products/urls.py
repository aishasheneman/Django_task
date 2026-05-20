from django.urls import path
from . import views

urlpatterns = [
    # 1. عرض قائمة المنتجات
    path('', views.product_list, name='product_list'),
    
    # 2. إضافة منتج جديد
    path('create/', views.product_create, name='product_create'),
    
    # 3. تعديل منتج قائم (يتوقع المعرف الأساسي pk)
    path('<int:pk>/update/', views.product_update, name='product_update'),
    
    # 4. حذف منتج (يتوقع المعرف الأساسي pk)
    path('<int:pk>/delete/', views.product_delete, name='product_delete'),
]