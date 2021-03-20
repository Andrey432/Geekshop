from django.db import models
from geekshop import settings
from mainapp.models import Product


class Basket(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="basket")
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(verbose_name="количество", default=0)
    add_date = models.DateTimeField(auto_now_add=True, verbose_name="время добавления")

    def __str__(self):
        return f'{self.product} (User: {self.user})'

    @property
    def price(self):
        return self.product.price * self.quantity

    @property
    def total_price(self):
        return sum(map(lambda p: p.price, Basket.objects.filter(user=self.user)))

    @property
    def total_quantity(self):
        return sum(map(lambda p: p.quantity, Basket.objects.filter(user=self.user)))
