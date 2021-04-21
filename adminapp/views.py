from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from adminapp.forms import ShopUserAdminEditForm, ProductCategoryEditForm, ProductEditForm
from authapp.forms import ShopUserRegisterForm
from authapp.models import ShopUser
from mainapp.models import ProductCategory, Product


def _is_super(user):
    return user.is_superuser


@user_passes_test(_is_super)
def user_create(request):
    if request.method == 'POST':
        form = ShopUserRegisterForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('adminapp:users'))
    else:
        form = ShopUserRegisterForm()
    context = {
        'title': "создание пользователя",
        'form': form
    }
    return render(request, 'adminapp/user_edit.html', context=context)


@user_passes_test(_is_super)
def users(request):
    users_list = ShopUser.objects.all().order_by('-is_active', '-is_superuser', '-is_staff', 'username')

    context = {
        'title': "пользователи",
        'objects': users_list
    }
    return render(request, 'adminapp/users.html', context=context)


@user_passes_test(_is_super)
def user_update(request, pk):
    user = get_object_or_404(ShopUser, pk=pk)

    if request.method == 'POST':
        form = ShopUserAdminEditForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('adminapp:users'))
    else:
        form = ShopUserAdminEditForm(instance=user)

    context = {
        'title': "редактиование пользователя",
        'form': form
    }
    return render(request, 'adminapp/user_edit.html', context=context)


@user_passes_test(_is_super)
def user_delete(request, pk):
    user = get_object_or_404(ShopUser, pk=pk)

    if request.method == 'POST':
        user.is_active = False
        user.save()
        return HttpResponseRedirect(reverse('adminapp:users'))

    context = {
        'title': "Удаление пользователя",
        'user_to_delete': user
    }
    return render(request, 'adminapp/user_delete.html', context=context)


@user_passes_test(_is_super)
def category_create(request):
    if request.method == 'POST':
        form = ProductCategoryEditForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('adminapp:categories'))
    else:
        form = ProductCategoryEditForm()

    context = {
        'title': "Создание категории",
        'form': form
    }
    return render(request, 'adminapp/category_edit.html', context=context)


@user_passes_test(_is_super)
def categories(request):
    context = {
        'title': "Все категории",
        'objects': ProductCategory.objects.all(),
    }
    return render(request, 'adminapp/categories.html', context=context)


@user_passes_test(_is_super)
def category_update(request, pk):
    category = get_object_or_404(ProductCategory, pk=pk)
    if request.method == 'POST':
        form = ProductCategoryEditForm(request.POST, request.FILES, instance=category)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('adminapp:categories'))
    else:
        form = ProductCategoryEditForm(instance=category)

    context = {
        'title': "Изменение категории",
        'form': form
    }
    return render(request, 'adminapp/category_edit.html', context=context)


@user_passes_test(_is_super)
def category_delete(request, pk):
    category = get_object_or_404(ProductCategory, pk=pk)
    if request.method == 'POST':
        category.is_active = False
        category.save()
        return HttpResponseRedirect(reverse('adminapp:categories'))

    context = {
        'title': "Удаление категории",
        'ctg_to_delete': category
    }
    return render(request, 'adminapp/category_delete.html', context=context)


@user_passes_test(_is_super)
def product_create(request, pk):
    category = get_object_or_404(ProductCategory, pk=pk)
    if request.method == 'POST':
        form = ProductEditForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('adminapp:products', args=[pk]))
    else:
        form = ProductEditForm()

    context = {
        'title': "Создание товара",
        'category': category,
        'form': form
    }
    return render(request, 'adminapp/product_edit.html', context=context)


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
def product_read(request, pk):
    context = {
        'title': "Информация о товаре",
        'object': get_object_or_404(Product, pk=pk)
    }
    return render(request, 'adminapp/product_detail.html', context=context)


@user_passes_test(_is_super)
def product_update(request, pk):
    product = get_object_or_404(Product, pk=pk)
    category = product.category

    if request.method == 'POST':
        form = ProductEditForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('adminapp:products', args=[category.pk]))
    else:
        form = ProductEditForm(instance=product)

    context = {
        'title': "Создание товара",
        'category': category,
        'form': form
    }
    return render(request, 'adminapp/product_edit.html', context=context)


@user_passes_test(_is_super)
def product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        product.is_active = False
        product.save()
        return HttpResponseRedirect(reverse('adminapp:products', args=[product.category.pk]))

    context = {
        'title': "Удаление категории",
        'category': product.category,
        'product_to_delete': product
    }
    return render(request, 'adminapp/product_delete.html', context=context)
