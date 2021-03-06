from django.urls import path
from mainapp import views

app_name = 'mainapp'

urlpatterns = [
    path('', views.products, name='products'),
    path('<int:pk>/', views.products, name='categories'),
    path('product/<int:pk>/', views.product, name='product')
]
