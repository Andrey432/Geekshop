from django.db import models


class ProductCategory(models.Model):
    name = models.CharField(max_length=32, unique=True, verbose_name="Название категории")
    description = models.TextField(blank=True, verbose_name="Описание категории")

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    name = models.CharField(max_length=64, verbose_name="Имя товара")
    short_desc = models.CharField(max_length=256, blank=True, verbose_name="Краткое описание товара")
    description = models.TextField(blank=True, verbose_name="Описание товара")
    image = models.ImageField(upload_to="products_previews", blank=True, verbose_name="Картинка товара")
    price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name="Цена товара")
    quantity = models.PositiveSmallIntegerField(default=0, verbose_name="Количество на складе")

    def __str__(self):
        return f'{self.name} ({self.category})'
