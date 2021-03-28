from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render, get_object_or_404
from django.template.loader import render_to_string
from django.urls import reverse

from basketapp.models import Basket
from mainapp.models import Product


@login_required
def view(request):
    context = {
        "title": 'корзина',
        "items": Basket.objects.filter(user=request.user).order_by('product__category')
    }
    return render(request, 'basketapp/basket.html', context=context)


@login_required
def basket_add(request, pk):
    if 'login' in request.META.get('HTTP_REFERER'):
        return HttpResponseRedirect(reverse('products:categories', args=[0]))

    product = get_object_or_404(Product, pk=pk)
    basket_item = Basket.objects.filter(product=product, user=request.user).first()
    if basket_item is None:
        basket_item = Basket(user=request.user, product=product)
    basket_item.quantity += 1
    basket_item.save()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required
def basket_remove(request, pk):
    product = get_object_or_404(Basket, pk=pk)
    product.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required
def basket_edit(request, pk, quantity):
    if request.is_ajax():
        basket = Basket.objects.filter(user=request.user).order_by('product__category')

        item = basket.filter(pk=pk).first()
        if item is not None:
            quantity = int(quantity)
            if quantity < 1:
                item.delete()
            else:
                item.quantity = int(quantity)
                item.save()

        context = {
            'items': basket
        }
        result = render_to_string('basketapp/includes/inc_basket_list.html', context=context)
        return JsonResponse({"result": result})
