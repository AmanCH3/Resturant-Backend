from django.urls import path
from . import views

urlpatterns = [
    path('orders/manage/', views.manage_orders, name='manage_orders'),
    path('orders/update/<int:order_id>/', views.update_order_status, name='update_order_status'),
]
