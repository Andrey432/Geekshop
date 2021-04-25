from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import ListView, UpdateView, CreateView, DeleteView, DetailView

from adminapp.forms import ShopUserAdminEditForm, ProductCategoryEditForm, ProductEditForm
from authapp.forms import ShopUserRegisterForm
from authapp.models import ShopUser
from mainapp.models import ProductCategory, Product


def _is_super(user):
    return user.is_superuser


class ShopUsersListView(ListView):
    model = ShopUser
    template_name = 'adminapp/users.html'

    @method_decorator(user_passes_test(_is_super))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


class ShopUserCreateView(CreateView):
    model = ShopUser
    template_name = 'adminapp/user_edit.html'
    success_url = 'adminapp:users'
    form_class = ShopUserRegisterForm

    @method_decorator(user_passes_test(_is_super))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


class ShopUserUpdateView(UpdateView):
    model = ShopUser
    template_name = 'adminapp/user_edit.html'
    success_url = reverse_lazy('adminapp:users')
    form_class = ShopUserAdminEditForm

    @method_decorator(user_passes_test(_is_super))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


class ShopUserDeleteView(DeleteView):
    model = ShopUser
    template_name = 'adminapp/user_delete.html'
    success_url = reverse_lazy('adminapp:users')

    @method_decorator(user_passes_test(_is_super))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        object_ = self.get_object()
        object_.is_active = False
        object_.save()
        return HttpResponseRedirect(self.success_url)


class ProductCategoryListView(ListView):
    model = ProductCategory
    template_name = 'adminapp/categories.html'

    @method_decorator(user_passes_test(_is_super))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


class ProductCategoryCreateView(CreateView):
    model = ProductCategory
    template_name = 'adminapp/category_edit.html'
    success_url = reverse_lazy('adminapp:categories')
    form_class = ProductCategoryEditForm

    @method_decorator(user_passes_test(_is_super))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


class ProductCategoryUpdateView(UpdateView):
    model = ProductCategory
    template_name = 'adminapp/category_edit.html'
    success_url = reverse_lazy('adminapp:categories')
    form_class = ProductCategoryEditForm

    @method_decorator(user_passes_test(_is_super))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Редактирование категории'
        return context


class ProductCategoryDeleteView(DeleteView):
    model = ProductCategory
    template_name = 'adminapp/category_delete.html'
    success_url = reverse_lazy('adminapp:categories')

    @method_decorator(user_passes_test(_is_super))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        object_ = self.get_object()
        object_.is_active = False
        object_.save()
        return HttpResponseRedirect(self.success_url)


@user_passes_test(_is_super)
def product_read(request, pk):
    context = {
        'title': "Информация о товаре",
        'object': get_object_or_404(Product, pk=pk)
    }
    return render(request, 'adminapp/product_detail.html', context=context)


class ProductsListView(ListView):
    model = Product
    template_name = 'adminapp/products.html'

    @method_decorator(user_passes_test(_is_super))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = get_object_or_404(ProductCategory, pk=self.kwargs['pk'])
        return context


class ProductsDetailView(DetailView):
    model = Product
    template_name = 'adminapp/product_detail.html'

    @method_decorator(user_passes_test(_is_super))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


class ProductCreateView(CreateView):
    model = Product
    template_name = 'adminapp/product_edit.html'
    success_url = 'adminapp:products'
    form_class = ProductEditForm

    @method_decorator(user_passes_test(_is_super))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = get_object_or_404(ProductCategory, pk=self.kwargs['pk'])
        return context


class ProductUpdateView(UpdateView):
    model = Product
    template_name = 'adminapp/product_edit.html'
    success_url = 'adminapp:products'
    form_class = ProductEditForm

    @method_decorator(user_passes_test(_is_super))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'adminapp/product_delete.html'
    success_url = 'adminapp:products'

    @method_decorator(user_passes_test(_is_super))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        object_ = self.get_object()
        object_.is_active = False
        object_.save()
        return HttpResponseRedirect(self.success_url)
