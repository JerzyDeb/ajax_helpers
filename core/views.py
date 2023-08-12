"""Core views."""

# Django
from django.views.generic import ListView

# Local
from .ajax_helpers import AjaxCreateView
from .ajax_helpers import AjaxDeleteView
from .ajax_helpers import AjaxDetailView
from .ajax_helpers import AjaxUpdateView
from .forms import TestModelForm
from .models import TestModel


class IndexView(ListView):  # noqa: D101
    model = TestModel
    template_name = 'base.html'


class TestModelDetailView(AjaxDetailView):  # noqa: D101
    model = TestModel
    template_name = 'detail.html'


class TestModelUpdateView(AjaxUpdateView):  # noqa: D101
    model = TestModel
    form_class = TestModelForm
    template_name = 'update.html'
    partial_template_name = '_partials/list_partial.html'

    def get_queryset(self):  # noqa: D102
        return self.model.objects.all()


class TestModelDeleteView(AjaxDeleteView):  # noqa: D101
    model = TestModel
    template_name = 'delete.html'
    partial_template_name = '_partials/list_partial.html'

    def get_queryset(self):  # noqa: D102
        return self.model.objects.all()


class TestModelCreateView(AjaxCreateView):  # noqa: D101
    model = TestModel
    template_name = 'create.html'
    form_class = TestModelForm
    partial_template_name = '_partials/list_partial.html'

    def get_queryset(self):  # noqa: D102
        return self.model.objects.all()
