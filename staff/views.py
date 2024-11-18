from django.contrib.admin.views.decorators import staff_member_required
from orders.models import Cart
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.shortcuts import get_object_or_404


# Create your views here.
@staff_member_required
def manage_orders(request):
    orders = Cart.objects.all().order_by("-order_date")
    if request.method == "POST":
        order_id = request.POST.get("order_id")
        new_status = request.POST.get("status")
        order = Cart.objects.get(pk=order_id)
        order.status = new_status
        order.save()
        return JsonResponse({"message": "Order status updated successfully!"})
    
    context = {
        "orders" : orders ,
        "status_choices": Cart.STATUS_CHOICES
    }
    return JsonResponse({"message": "List of orders", "data": context})


# Update order status
@staff_member_required
@require_POST
def update_order_status(request, order_id):
    order = get_object_or_404(Cart, pk=order_id)
    status = request.POST.get("status")
    if status in dict(Cart.STATUS_CHOICES):
        order.status = status
        order.save()
        return JsonResponse({"message": "Order status updated successfully."})
    return JsonResponse({"error": "Invalid status."}, status=400)