from django.contrib import admin
from backoffice import models


@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = 'first_name', 'last_name', 'phone', 'email', 'city', 'country',
    search_fields = 'first_name', 'last_name', 'phone', 'email',
    list_per_page = 20
    list_max_show_all = 200
    list_display_links = 'first_name',


@admin.register(models.Category)
class CategotyAdmin(admin.ModelAdmin):
    list_display = 'name',
