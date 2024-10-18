from django.db import models
from .category import Category  # Ensure this is correct

class Product(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    image = models.ImageField(upload_to='img')
    desc = models.TextField()
    price = models.IntegerField()

    def __str__(self):
        return self.name
