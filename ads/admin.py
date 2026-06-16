from django.contrib import admin
from .models import Category, Ad


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


@admin.register(Ad)
class AdAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title',
        'author',
        'category',
        'price',
        'is_active',
        'created_at',
    )

    list_filter = ('category', 'is_active')
    search_fields = ('title', 'description')