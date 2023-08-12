"""Core models."""

# Django
from django.db import models
from django.utils.translation import gettext_lazy as _


class TestModel(models.Model):  # noqa: D101
    name = models.CharField(
        _('Name'),
        max_length=64,
    )
    description = models.TextField(
        _('Description'),
    )
    number = models.IntegerField(
        _('Number')
    )

    class Meta:  # noqa: D106
        verbose_name = _('Test model')
        verbose_name_plural = _('Test models')

    def __str__(self):  # noqa: D105
        return f'{self.name}'
