from django.shortcuts import render
from .models import Products
from .forms import ProductForm, RawProductForm


def dynamic_product_lookup(request, my_id):
    obj = Products.objects.get(id=my_id)
    context = {
        'object': obj
    }
    return render(request, 'products/view.html', context)


def product_create_view(request):
    initial_data = {
        'title': 'This is an awesome title'
    }

    # for changing some certain product from the database.
    # obj = Products.objects.get(id=1)
    # form = ProductForm(request.POST or None, instance=obj)

    # setting the initial values of the fields.

    form = ProductForm(request.POST or None, initial= initial_data)
    if form.is_valid():
        form.save()
        form = ProductForm()
    context = {
        'form': form
    }
    return render(request, 'products/product_create.html', context)


# Create your views here.
#
# def product_create_view(request):
#     title = None
#     if request.method == 'POST':
#         title = request.POST.get('title')
#         print(title)
#     context = {'title': title}
#     return render(request, 'products/product_create.html', context)

#
# def product_create_view(request):
#     form = RawProductForm()
#     if request.method == "POST":
#         form = RawProductForm(request.POST)
#         if form.is_valid():
#             print(form.cleaned_data)
#             Products.objects.create(**form.cleaned_data)
#             form = RawProductForm()
#         else:
#             print(form.errors)
#     context = {
#         'form': form
#     }
#     return render(request, 'products/product_create.html', context)


def product_detail_view(request):
    obj = Products.objects.get(id=1)
    context = {
        'object': obj
    }
    return render(request, 'products/product_details.html', context)
