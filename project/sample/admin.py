from django.contrib import admin
from .models import Person

# Register your models here.

@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email', 'created_at']
    list_filter = ['created_at', 'updated_at']
    search_fields = ['first_name', 'last_name', 'email']
    ordering = ['last_name', 'first_name']
    readonly_fields = ['created_at', 'updated_at']
