from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, get_object_or_404
from .models import Product, ProductCategory, CompanyContact
import random


def _random_products(count):
    products_list = list(Product.objects.all())
    random.shuffle(products_list)
    return products_list[:count]


def main(request):
    context = {
        "page": 'home',
        "title": 'главная',
        "most_populars": _random_products(3),
    }
    return render(request, 'mainapp/index.html', context=context)


def contact(request):
    context = {
        "page": 'contact',
        "title": 'контакты',
        "contacts_list": CompanyContact.objects.all(),
    }
    return render(request, 'mainapp/contact.html', context=context)


def products(request, pk=None):
    ctg_all = {"name": 'все', "pk": 0}
    context = {
        "page": 'products',
        "title": 'товары',
        "categories": [ctg_all] + list(ProductCategory.objects.all()),
        "cur_category": pk,
        "similar": _random_products(3)
    }

    if pk is not None:
        if pk == 0:
            category = ctg_all
            products_list = Product.objects.all().order_by('price')
        else:
            category = get_object_or_404(ProductCategory, pk=pk)
            products_list = Product.objects.filter(category=category)

        page = request.GET.get('p', 1)
        paginator = Paginator(products_list, 2)
        try:
            products_paginator = paginator.page(page)
        except PageNotAnInteger:
            products_paginator = paginator.page(1)
        except EmptyPage:
            products_paginator = paginator.page(paginator.num_pages)

        context["selected_category"] = category
        context["products"] = products_paginator

        return render(request, 'mainapp/products_list.html', context=context)

    return render(request, 'mainapp/products.html', context=context)


def product(request, pk):
    item = get_object_or_404(Product, pk=pk)
    context = {
        'title': item.name,
        'product': item
    }
    return render(request, 'mainapp/product.html', context=context)
