from django.shortcuts import render, get_object_or_404, redirect
from .models import Item, Category


def item_list(request):
    query = request.GET.get("q")
    if query:
        items = Item.objects.filter(name__icontains=query) | Item.objects.filter(
            category__name__icontains=query
        )
    else:
        items = Item.objects.all()
    return render(request, "shop/item_list.html", {"items": items})


def item_detail(request, pk):
    item = get_object_or_404(Item, pk=pk)
    return render(request, "shop/item_detail.html", {"item": item})

def cart_detail(request):
    cart = request.session.get("cart", {})
    items = Item.objects.filter(id__in=cart.keys())
    total_amount = sum(item.price * cart[str(item.id)] for item in items)
    
    # Create a list of tuples (item, count)
    cart_items = [(item, cart[str(item.id)]) for item in items]
    
    return render(
        request, "shop/cart_detail.html", {"cart_items": cart_items, "total_amount": total_amount}
    )



def checkout(request):
    return render(request, "shop/checkout.html")



def add_to_cart(request, pk):
    item = get_object_or_404(Item, pk=pk)
    cart = request.session.get("cart", {})
    if str(item.id) in cart:
        cart[str(item.id)] += 1
    else:
        cart[str(item.id)] = 1
    request.session["cart"] = cart
    return redirect("cart_detail")

def reduce_quantity(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    
    # Assuming you have a session-based cart management system
    if item.id in request.session.get('cart', {}):
        request.session['cart'][item.id] -= 1
        if request.session['cart'][item.id] <= -1:
            del request.session['cart'][item.id]
    
    return redirect('cart_detail')  
def remove_item(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    
    # Assuming you have a session-based cart management system
    if item.id in request.session and item_id in request.session['cart']:
        del request.session['cart'][item.id]
    
    return redirect('cart_detail')  