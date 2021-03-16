from django.db import models
from .base_object import BaseObject

class Order(BaseObject):
    product_id = models.ForeignKey(
        'Product',
        on_delete=models.PROTECT,
    )
    product_size = models.TextField()
    name = models.TextField()
    email = models.TextField()
    phone = models.TextField()