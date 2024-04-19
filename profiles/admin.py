from django.contrib import admin
from .models import Profile

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'first_name', 'phone', 'country', 'email_two')
    search_fields = ('bio', 'country')


admin.site.register(Profile, ProfileAdmin)