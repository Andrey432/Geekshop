from django.core.management import BaseCommand
from django.db import IntegrityError

from geekshop.settings import BASE_DIR
from authapp.models import ShopUser
from mainapp.models import *
import json


def _load_json_datafile(main, file):
    path = BASE_DIR / f'{main}/json/{file}.json'
    with open(path, 'r', encoding='utf-8', errors='ignore') as f:
        return json.load(f)


class Command(BaseCommand):
    def handle(self, *args, **options):
        categories = _load_json_datafile('mainapp', 'products_categories')
        ProductCategory.objects.all().delete()
        for ctg in categories:
            ProductCategory.objects.create(**ctg)

        products = _load_json_datafile('mainapp', 'products')
        Product.objects.all().delete()
        for prod in products:
            prod['category'] = ProductCategory.objects.get(name=prod['category'])
            Product.objects.create(**prod)

        contacts = _load_json_datafile('mainapp', 'contacts_info')
        CompanyContact.objects.all().delete()
        for cnt in contacts:
            CompanyContact.objects.create(**cnt)

        try:
            ShopUser.objects.create_superuser(username='django', password="geekbrains", age=18)
        except IntegrityError as e:
            print(f'{type(e).__name__}: {e}')
