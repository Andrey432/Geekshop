from django.shortcuts import render
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
    context = {
        "page": 'products',
        "page_title": 'товары',
        "categories": ProductCategory.objects.all(),
        "cur_category": pk,
        "active_ctg": request.resolver_match.url_name
    }

    return render(request, 'mainapp/products.html', context=context)
