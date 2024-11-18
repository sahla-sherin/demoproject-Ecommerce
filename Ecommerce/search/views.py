from django.shortcuts import render
from django.db.models import Q
from shop.models import Product

def search_product(request):
    context = {'pro': [], 'query': ''}
    if request.method == "POST":
        query = request.POST['q']  # Get the query and remove unnecessary spaces
        if query:
            p = Product.objects.filter(Q(name__icontains=query) | Q(desc__icontains=query))
            context = {'pro': p, 'query': query}
    return render(request, 'search.html', context)
