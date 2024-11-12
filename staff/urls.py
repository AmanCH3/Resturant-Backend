from django.urls import path
from . import views

urlpatterns = [
    path('orders/', views.OrderListCreate.as_view(), name='orders-list-create'),
    
]