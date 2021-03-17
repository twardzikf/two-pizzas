from django.db import models

class Size(models.TextChoices):
    SMALL =  'small'
    MEDIUM = 'medium'
    LARGE = 'large'
    
class Product(models.Model):
    name = models.TextField()
    sizes = models.JSONField()

class Order(models.Model):
    product_id = models.ForeignKey(
        'Product',
        on_delete=models.PROTECT,
    )
    product_name = models.CharField(max_length=50)
    product_size = models.CharField(
        max_length=20,
        choices=Size.choices,
        default=Size.SMALL,
    )
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=320)
    phone = models.CharField(max_length=20)
