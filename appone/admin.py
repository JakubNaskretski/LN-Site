from django.contrib import admin
from appone.models import Product, ProductType
# Register your models here.
@admin.register(Product)
class PostAdmin(admin.ModelAdmin):
    list_display = ('product_id', 'product_name', 'product_type')

    ordering = ('product_id', 'product_type')


admin.site.register(ProductType)
