from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'stock', 'category']
        labels = {
            'name': 'اسم المنتج',
            'description': 'الوصف',
            'price': 'السعر ($)',
            'stock': 'الكمية في المخزون',
            'category': 'تصنيف المنتج',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'stock': forms.NumberInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}), # تحويله لقائمة منسدلة
        }