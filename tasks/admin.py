from django.contrib import admin
from .models import Review

@admin.register(Review)
class TaskAdmin(admin.ModelAdmin):
    search_fields = ["author"]
    list_display = ["id", "author", "text"]