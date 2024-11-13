from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Order, OrderItem
from customers.models import Customer
from menus.models import MenuItem
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404

@login_required
@csrf_exempt
# This view function is used to place an order for a customer
def place_order(request):
    if request.method == "POST":
        customer = request.user.customer  # assuming Customer is linked to the user model
        menu_item_id = request.POST.get('menu_item_id')
        quantity = int(request.POST.get('quantity', 1))
        menu_item = MenuItem.objects.get(id=menu_item_id)
        
        # Create or update order for the customer
        order = Order.objects.create(customer=customer, order_value=menu_item.price * quantity)
        OrderItem.objects.create(order=order, menu_item=menu_item, quantity=quantity)

        return JsonResponse({"message": "Order placed successfully!"})
    return JsonResponse({"message": "Invalid request!"})


#for the order details
@login_required
def order_detail(request, order_id):
    order = get_object_or_404(Order, pk=order_id, customer=request.user.customer)
    order_items = OrderItem.objects.filter(order=order)
    
    context = {
        "order": order,
        "order_items": order_items,
    }
    return JsonResponse({"message" : "Order details", "data": context})

#for the order list filter according to the customer
@login_required
def order_list(request):
    orders = Order.objects.filter(customer=request.user.customer).order_by("-order_date")
    context = {"orders": orders}
    return JsonResponse({"message": "List of orders", "data": context})



#Tracking the order
@login_required
def track_order(request, order_id):
    order = get_object_or_404(Order, pk=order_id, customer=request.user.customer)
    return JsonResponse({
        "status": order.status,
        "order_number": order.order_number,
        "order_date": order.order_date,
    })
