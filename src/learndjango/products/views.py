from django.shortcuts import render
from .models import Products


# Create your views here.
def product_detail_view(request):
    obj = Products.objects.get(id=1)
    context = {
        'object': obj
    }
    print(obj.title)
    return render(request, 'products/product_details.html', context)
