from django.contrib import admin
from mptt.admin import MPTTModelAdmin

# Register your models here.
from .models import Category, Advert, FilterAdvert

@admin.register(Category)
class CategoryAdmin(MPTTModelAdmin):
    list_display = ('name', 'id',)
    mptt_level_indent = 20
    prepopulated_fields = {'slug':('name',)}


@admin.register(Advert)
class AdvertAdmin(admin.ModelAdmin):
    """Объявления"""
    list_display = (
        "id",
        "subject",
        "user",
        "category",
        "filters",
        "price",
        "created",
        "moderation"
    )
    list_display_links = ("subject",)
    list_filter = ("user", "category", "filters", "price")
    prepopulated_fields = {"slug": ("user", "subject")}
    search_fields = ("user", "category", "subject", "created")


@admin.register(FilterAdvert)
class FilterAdvertAdmin(admin.ModelAdmin):
    list_display = ("name", "id")
    list_display_links = ("name",)
    prepopulated_fields = {"slug": ("name",)}
    search_fields = ("name",)

