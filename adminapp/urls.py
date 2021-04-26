from django.urls import path
from adminapp import views


app_name = 'adminapp'

urlpatterns = [
    path('users/all/', views.ShopUsersListView.as_view(), name='users'),
    path('users/create/', views.ShopUserCreateView.as_view(), name='user_create'),
    path('users/update/<int:pk>/', views.ShopUserUpdateView.as_view(), name='user_update'),
    path('users/delete/<int:pk>/', views.ShopUserDeleteView.as_view(), name='user_delete'),

    path('categories/all/', views.ProductCategoryListView.as_view(), name='categories'),
    path('categories/create/', views.ProductCategoryCreateView.as_view(), name='category_create'),
    path('categories/update/<int:pk>/', views.ProductCategoryUpdateView.as_view(), name='category_update'),
    path('categories/delete/<int:pk>/', views.ProductCategoryDeleteView.as_view(), name='category_delete'),

    path('products/read/category/<int:pk>/', views.ProductsListView.as_view(), name='products'),
    path('products/read/<int:pk>/', views.ProductDetailView.as_view(), name='product_read'),
    path('products/create/category/<int:pk>/', views.ProductCreateView.as_view(), name='product_create'),
    path('products/update/<int:pk>/', views.ProductUpdateView.as_view(), name='product_update'),
    path('products/delete/<int:pk>/', views.ProductDeleteView.as_view(), name='product_delete'),

]

