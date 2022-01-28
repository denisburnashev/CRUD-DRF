from django.contrib import admin
from .models import Product, Stock, StockProduct
# Register your models here.


class StockProductInline(admin.TabularInline):
    model = StockProduct


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [StockProductInline]


@admin.register(Stock)
class StockAdmin(admin.ModelAdmin):
    inlines = [StockProductInline]


@admin.register(StockProduct)
class StockProductInlineAdmin(admin.ModelAdmin):
    pass