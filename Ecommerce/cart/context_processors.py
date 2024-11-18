
from cart.models import Cart

def count_items(request):
    count = 0  # Initialize count with a default value

    if request.user.is_authenticated:
        try:
            c = Cart.objects.filter(user=request.user)
            for i in c:
                count += i.quantity
        except Exception as e:
            # Optional: log or print the exception for debugging
            print(f"Error in count_items: {e}")

    return {'count': count}



