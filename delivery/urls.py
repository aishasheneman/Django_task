from django.urls import path
from . import views

urlpatterns = [
    path('', views.DeliveryOrderListView.as_view(), name='delivery_order_list'),
    path('create/', views.DeliveryOrderCreateView.as_view(), name='delivery_create'),
    path('update/<int:pk>/', views.DeliveryOrderUpdateView.as_view(), name='delivery_update'),
    path('delete/<int:pk>/', views.DeliveryOrderDeleteView.as_view(), name='delivery_delete'),
    path('DeliveryOrderSerializer/',views.delivery_api_list.as_view(), name= 'delivery_api_list'),
]