from django.shortcuts import render, get_object_or_404

from basketapp.models import Basket
from .models import Product, ProductCategory, CompanyContact


def main(request):
    context = {
        "page": 'home',
        "page_title": 'главная',
        "products": Product.objects.all()[:3],
    }
    return render(request, 'mainapp/index.html', context=context)


def contact(request):
    context = {
        "page": 'contact',
        "page_title": 'контакты',
        "contacts_list": CompanyContact.objects.all(),
    }
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
        "cur_category": pk
    }

    if request.user.is_authenticated:
        context["basket"] = sum(Basket.objects.filter(user=request.user).values_list('quantity', flat=True))

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
