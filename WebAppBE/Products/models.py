from django.db import models
from Auth.models import CustomUser


class Order(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE) # Many-to-One
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    completed = models.BooleanField(default=False)
    on_promo_terms = models.BooleanField(default=False)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    products_group_id = models.OneToOneField("ProductsGroup", on_delete=models.CASCADE)

    def __str__(self):
        return self.id # id формируется Джанго, но могу ли я к нему так обратиться и такое ли у этого аттрибута имя?


class ProductsGroup(models.Model):
    product = models.ManyToManyField("Product", related_name="products_group")

    def __str__(self):
        return self.id


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

# когда удаляю файлы миграции, Джанго по разному воспримит при попытке создать миграции: (1) отсутствие только самих файлов миграций; (2) + отсутствие файла init  папке миграций; (3) + отсутствие самой папки миграций