from django.contrib import admin
from .models import DeliveryOrder

@admin.register(DeliveryOrder)
class DeliveryOrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer', 'product', 'quantity', 'status', 'order_date','delivery_driver_name')
    list_filter = ('status', 'order_date')
    search_fields = ('id', 'customer__first_name')
    fieldsets = (
        ('تفاصيل الطلب الأساسية', {
            'fields': ('customer', 'product', 'quantity', 'status')
        }),
        ('بيانات مندوب التوصيل', {
            'fields': ('delivery_driver_name', 'delivery_driver_phone', 'vehicle_number')
        }),
    )