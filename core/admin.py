"""Core admin."""

# Django
from django.contrib import admin

# Project
from core.models import TestModel

# Register your models here.


@admin.register(TestModel)
class TestModelAdmin(admin.ModelAdmin):  # noqa: D101
    list_display = [
        'name',
        'number',
    ]
