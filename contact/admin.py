from django.contrib import admin
from contact import models

# Register your models here.
@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'phone', 'email', 'created_date', 'show')
    ordering = ('-id',)
    search_fields = ('first_name', 'last_name', 'phone', 'email')
    #list_filter = ('created_date', 'show')
    list_per_page = 10
    list_max_show_all = 200
    list_editable = ('show',)
    list_display_links = ('id', 'first_name', 'last_name')

@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    ordering = ('-id',)
    list_display_links = ('name',)