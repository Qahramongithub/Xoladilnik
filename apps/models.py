from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)
    icon = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class SubCategory(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey('apps.Category', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Brand(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='brand/', null=True, blank=True)

    def __str__(self):
        return self.name


class Nutrition(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='products/')
    price = models.DecimalField(max_digits=5, decimal_places=2)
    count = models.IntegerField(default=0)
    sub_category = models.ForeignKey('apps.SubCategory', on_delete=models.CASCADE)
    brand = models.ForeignKey('apps.Brand', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class NutritionItem(models.Model):
    nutrition = models.ForeignKey('apps.Nutrition', on_delete=models.CASCADE)
    product = models.ForeignKey('apps.Product', on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.nutrition.name
