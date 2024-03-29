from django.contrib import admin
from mptt.admin import MPTTModelAdmin

# Register your models here.
from .models import Category, Advert

@admin.register(Category)
class CategoryAdmin(MPTTModelAdmin):
    list_display = ('id', 'name',)
    mptt_level_indent = 20


@admin.register(Advert)
class AdvertAdmin(admin.ModelAdmin):
    list_display = ('id', 'subject', 'user', 'category', 'price', 'created', 'moderation')
    list_display_links = ('subject',)
    list_filter = ('user', 'category', 'price', )
