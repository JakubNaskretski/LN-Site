from django.db import models
from django.urls import reverse
# Create your models here.

class ProductType(models.Model):
    product_type = models.CharField(primary_key=True, max_length=30)

    def __str__(self):
        return self.product_type

class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=25, unique=True)
    product_ingredients = models.CharField(max_length=250)
    product_description = models.CharField(max_length=250)
    product_type = models.ForeignKey(ProductType, on_delete=models.DO_NOTHING)
    product_image = models.ImageField(upload_to='products')

    def __str__(self):
        return self.product_name

# code for post model from book
    # def get_absolute_url(self):
    #     return reverse('blog:post_detail',
    #     args=[self.publish.year,
    #     self.publish.month,
    #     self.publish.day,
    #     self.slug])
