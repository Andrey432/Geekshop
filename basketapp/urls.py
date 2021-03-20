from django.urls import path
from basketapp import views


app_name = 'basketapp'

urlpatterns = [
    path('', views.basket, name='basket_view'),
    path('add/<int:pk>/', views.basket_add, name='basket_add'),
    path('remove/<int:pk>/', views.basket_remove, name='basket_remove'),
]
