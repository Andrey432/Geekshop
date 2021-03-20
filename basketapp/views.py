from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from basketapp.models import Basket
from mainapp.models import Product


def basket(request):
    context = {
        "title": 'корзина',
        "basket_items": Basket.objects.filter(user=request.user)
    }
    return render(request, 'basketapp/basket.html', context=context)


def basket_add(request, pk):
    product = get_object_or_404(Product, pk=pk)
    basket_item = Basket.objects.filter(product=product, user=request.user).first()
    if basket_item is None:
        basket_item = Basket(user=request.user, product=product)
    basket_item.quantity += 1
    basket_item.save()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def basket_remove(request, pk):
    product = get_object_or_404(Basket, pk=pk)
    product.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
