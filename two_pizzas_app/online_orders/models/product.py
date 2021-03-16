from django.db import models
from .base_object import BaseObject

class Product(BaseObject):
    name = models.TextField()
    #sizes = models.ArrayField()