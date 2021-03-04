from django.shortcuts import render
from json_file_loader import load_json_data


def main(request):
    context = {
        "page": 'home',
        "page_title": 'главная'
    }
    return render(request, 'mainapp/index.html', context=context)


def contact(request):
    context = {
        "page": 'contact',
        "page_title": 'контакты',
        "contacts_list": load_json_data('contacts_list', []),
    }
    return render(request, 'mainapp/contact.html', context=context)


def products(request):
    context = {
        "page": 'products',
        "page_title": 'товары',
        "categories": load_json_data('product_categories', []),
        "active_ctg": request.resolver_match.url_name
    }

    if request.resolver_match.url_name == 'products':
        context["active_ctg"] = 'products_all'

    return render(request, 'mainapp/products.html', context=context)
