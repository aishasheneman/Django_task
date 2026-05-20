from django.db import models

class PersonInfo(models.Model):
    first_name = models.CharField(max_length=50, verbose_name="الاسم الأول")
    last_name = models.CharField(max_length=50, verbose_name="الاسم الأخير")
    phone = models.CharField(max_length=15, verbose_name="رقم الهاتف")
    address = models.TextField(verbose_name="العنوان")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="تاريخ الإضافة")

    class Meta:
        abstract = True  

class Customer(PersonInfo):
    email = models.EmailField(unique=True, verbose_name="البريد الإلكتروني")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"