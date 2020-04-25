from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404
from .models import Products
from .forms import ProductForm, RawProductForm


def all_product_detail_view(request):
    objects = Products.objects.all()
    context = {
        'object': objects
    }
    return render(request, 'products/all_products.html', context)


def product_deletion(request, my_id):
    obj = get_object_or_404(Products, id=my_id)
    if request.method == "POST":
        obj.delete()
        redirect('../../')
    context = {
        'object': obj
    }
    return render(request, 'products/delete.html', context)


def dynamic_product_lookup(request, my_id):
    # obj = Products.objects.get(id=my_id)
    # if the value not found it can give you 404 error.
    obj = get_object_or_404(Products, id=my_id)

    # or you can use try and catch to check that the page exist or not.
    # try:
    #     obj = Products.objects.get(id=my_id)
    # except Products.DoesNotExist:
    #     raise Http404
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
    obj = Products.objects.get(id=3)
    context = {
        'object': obj
    }
    return render(request, 'products/product_details.html', context)
