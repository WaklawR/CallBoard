from django.contrib import admin

# Register your models here.
from django.contrib import admin

from .models import Photo



@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ("name", "created", "id")
    list_filter = ("name", "created")
    search_fields = ("name", "created")
