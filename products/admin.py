from django.contrib import admin
from .models import Product, ProductImage, Category

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_at'
    search_fields = ["title","description"]
    list_display = ['name', 'price','active', 'created_at']
    list_editable = ['price','active']
    list_filter = ['price', 'active']
    readonly_fields = ['created_at','updated_at']

    class Meta:
        model = Product

admin.site.register(Product, ProductAdmin)
admin.site.register(ProductImage)
admin.site.register(Category)