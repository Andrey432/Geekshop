from django.shortcuts import render, get_object_or_404
from basketapp.models import Basket
from .models import Product, ProductCategory, CompanyContact
import random


def _random_products(count):
    products_list = list(Product.objects.all())
    random.shuffle(products_list)
    return products_list[:count]


def main(request):
    context = {
        "page": 'home',
        "page_title": 'главная',
        "most_populars": _random_products(3),
    }
    if request.user.is_authenticated:
        context["basket"] = Basket.objects.filter(user=request.user)
    return render(request, 'mainapp/index.html', context=context)


def contact(request):
    context = {
        "page": 'contact',
        "page_title": 'контакты',
        "contacts_list": CompanyContact.objects.all(),
    }
    if request.user.is_authenticated:
        context["basket"] = Basket.objects.filter(user=request.user)
    return render(request, 'mainapp/contact.html', context=context)


def products(request, pk=None):
    ctg_all = {
        "name": 'все',
        "pk": 0,
    }
    context = {
        "page": 'products',
        "page_title": 'товары',
        "categories": [ctg_all] + list(ProductCategory.objects.all()),
        "cur_category": pk,
        "similar": _random_products(3)
    }

    if request.user.is_authenticated:
        context["basket"] = Basket.objects.filter(user=request.user)

    if pk is not None:
        if pk == 0:
            category = ctg_all
            products_list = Product.objects.all().order_by('price')
        else:
            category = get_object_or_404(ProductCategory, pk=pk)
            products_list = Product.objects.filter(category=category)

        context["selected_category"] = category
        context["products"] = products_list
        return render(request, 'mainapp/products_list.html', context=context)

    return render(request, 'mainapp/products.html', context=context)


def product(request, pk):
    item = get_object_or_404(Product, pk=pk)
    context = {
        'page_title': item.name,
        'product': item
    }
    if request.user.is_authenticated:
        context["basket"] = Basket.objects.filter(user=request.user)
    return render(request, 'mainapp/product.html', context=context)
