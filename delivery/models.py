from django.db import models
from customers.models import Customer  
#from products.models import Product

class DeliveryOrder(models.Model):
    STATUS_CHOICES = [
        ('PENDING', 'قيد الانتظار'),
        ('SHIPPED', 'تم الشحن'),
        ('DELIVERED', 'تم التوصيل'),
    ]

    # --- العلاقات مع التطبيقات الأخرى ---
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, verbose_name="العميل")
    product = models.ForeignKey('products.Product', on_delete=models.CASCADE, verbose_name="المنتج")
    
    # --- تفاصيل الطلب والشحنة ---
    quantity = models.PositiveIntegerField(default=1, verbose_name="الكمية")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='PENDING', verbose_name="حالة الشحنة")
    order_date = models.DateTimeField(auto_now_add=True, verbose_name="تاريخ الطلب")

    # --- بيانات موظف التوصيل ---
    delivery_driver_name = models.CharField(max_length=100, blank=True, null=True, verbose_name="اسم مندوب التوصيل")
    delivery_driver_phone = models.CharField(max_length=15, blank=True, null=True, verbose_name="هاتف المندوب")
    vehicle_number = models.CharField(max_length=50, blank=True, null=True, verbose_name="رقم مركبة التوصيل")

    def __str__(self):
        return f"طلب توصيل #{self.id} للعميل {self.customer.first_name}"