from django.contrib import admin
from . import models

# Register your models here.


@admin.register(models.User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'create_time', 'address', 'balance')


@admin.register(models.Books)
class BooksAdmin(admin.ModelAdmin):
    list_display = ('ISBN', 'name', 'category', 'old_price', 'price', 'book_image', 'storage', 'sale_volume')
    list_filter = ('category',)


@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('order_number', 'user', 'trade_time', )
    list_filter = ('user', 'trade_time',)


@admin.register(models.BooksUser)
class BooksUserAdmin(admin.ModelAdmin):
    list_display = ('id', 'book', 'user', 'count')
    list_filter = ('user',)


@admin.register(models.BooksOrder)
class BooksOrderAdmin(admin.ModelAdmin):
    list_display = ('book', 'order', 'count')