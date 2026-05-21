from .models import DeliveryOrder
from rest_framework import serializers

class DeliveryOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeliveryOrder
        fields = '__all__'