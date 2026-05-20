from django.db import models

class Product(models.Model):
    CATEGORY_CHOICES = [
        ('تصميم واجهات', 'تصميم واجهات'),
        ('برمجيات وتطبيقات', 'برمجيات وتطبيقات'),
        ('استشارات رقمية', 'استشارات رقمية'),
        ('خدمات سحابية', 'خدمات سحابية'),
    ]
    
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField(default=0)
    category = models.CharField(max_length=100, choices=CATEGORY_CHOICES, blank=True, null=True)

    def __str__(self):
        return self.name