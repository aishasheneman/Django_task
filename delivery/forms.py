from django import forms
from .models import DeliveryOrder

class DeliveryOrderForm(forms.ModelForm):
    class Meta:
        model = DeliveryOrder
        fields = ['customer', 'product', 'quantity', 'status', 'delivery_driver_name', 'delivery_driver_phone', 'vehicle_number']
        # widgets = {
        #     'customer': forms.Select(attrs={'class': 'form-select'}),
        #     'product': forms.Select(attrs={'class': 'form-select'}),
        #     'quantity': forms.NumberInput(attrs={'class': 'form-control'}),
        #     'status': forms.Select(attrs={'class': 'form-select'}),
        #     'delivery_driver_name': forms.TextInput(attrs={'class': 'form-control'}),
        #     'delivery_driver_phone': forms.TextInput(attrs={'class': 'form-control'}),
        #     'vehicle_number': forms.TextInput(attrs={'class': 'form-control'}),
        # }