from django.urls import path , include
from . import views
from rest_framework import routers


r = routers.DefaultRouter()
r.register(r'users', views.user_list)

urlpatterns = [
    path('login/', views.login_view, name='login'),
path('logout/', views.logout_view, name='logout'),
path('register/', views.register_view, name='register'),
path('api/', include(r.urls))
]