from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render, get_object_or_404
from authapp.models import ShopUser
from mainapp.models import ProductCategory, Product


def _is_super(user):
    return user.is_superuser


@user_passes_test(_is_super)
def user_create(request):
    return render(request, '')


@user_passes_test(_is_super)
def users(request):
    users_list = ShopUser.objects.all().order_by('-is_active', '-is_superuser', '-is_staff', 'username')

    context = {
        'title': "пользователи",
        'objects': users_list
    }
    return render(request, 'adminapp/users.html', context=context)


@user_passes_test(_is_super)
def user_update(request):
    return render(request, '')


@user_passes_test(_is_super)
def user_delete(request):
    return render(request, '')


@user_passes_test(_is_super)
def category_create(request):
    return render(request, '')


@user_passes_test(_is_super)
def categories(request):
    context = {
        'title': "Категории",
        'objects': ProductCategory.objects.all(),
    }
    return render(request, 'adminapp/categories.html', context=context)


@user_passes_test(_is_super)
def category_update(request):
    return render(request, '')


@user_passes_test(_is_super)
def category_delete(request):
    return render(request, '')


@user_passes_test(_is_super)
def product_create(request):
    return render(request, '')


@user_passes_test(_is_super)
def products(request, pk):
    category = get_object_or_404(ProductCategory, pk=pk)
    objects = Product.objects.filter(category__pk=pk).order_by('name')
    context = {
        'title': f'{category.name}: Товары',
        'category': category,
        'objects': objects,
    }
    return render(request, 'adminapp/products.html', context=context)


@user_passes_test(_is_super)
def product_read(request):
    return render(request, '')


@user_passes_test(_is_super)
def product_update(request):
    return render(request, '')


@user_passes_test(_is_super)
def product_delete(request):
    return render(request, '')

