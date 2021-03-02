from django.shortcuts import render


def main(request):
    context = {
        "page": 'home',
        "page_title": 'главная'
    }
    return render(request, 'mainapp/index.html', context=context)


def contact(request):
    context = {
        "page": 'contact',
        "page_title": 'контакты'
    }
    return render(request, 'mainapp/contact.html', context=context)


def products(request):
    context = {
        "page": 'products',
        "page_title": 'товары'
    }
    return render(request, 'mainapp/products.html', context=context)
