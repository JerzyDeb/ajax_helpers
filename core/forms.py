"""Core forms."""

# Django
from django import forms

# Local
from .models import TestModel
from .utils import set_bootstrap_class


class TestModelForm(forms.ModelForm):  # noqa: D101
    class Meta:  # noqa: D106
        model = TestModel
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        """Add bootstrap classes to all fields."""
        super().__init__(*args, **kwargs)
        set_bootstrap_class(self.fields)
