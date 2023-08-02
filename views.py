from django.contrib.messages.views import SuccessMessageMixin
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.views import View
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView
from django.utils.translation import gettext_lazy as _


class AjaxBaseView(SuccessMessageMixin, View):
    template_name = None
    partial_template_name = None
    queryset = None
    title = None

    def get_queryset(self):
        return self.queryset

    def get_context_data(self, *args, **kwargs):
        return {}

    def get(self, request, *args, **kwargs):
        return JsonResponse({
            'html': render_to_string(
                self.template_name,
                self.get_context_data(),
                request,
            ),
        }, status=200)

    def form_valid(self, form):  # noqa: D102
        form.save()
        return JsonResponse({
            'html_object_list': render_to_string(
                self.partial_template_name,
                self.get_context_data(),
                self.request,
            ),
            'message': self.success_message,
            'title': self.title,
        }, status=200)

    def form_invalid(self, form):  # noqa: D102
        return JsonResponse({
            'html': render_to_string(
                self.template_name,
                self.get_context_data(),
                self.request,
            ),
        }, status=400)


class AjaxDetailView(AjaxBaseView, AjaxBaseView, DetailView):
    """Ajax View to show detail of an object."""
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data()
        context['object'] = self.get_object()
        return context


class AjaxCreateView(SuccessMessageMixin, AjaxBaseView, CreateView):
    """Ajax View to create an object and refresh content in partial_template_name."""
    title = _('Created')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data()
        context['form'] = self.get_form()
        return context


class AjaxUpdateView(SuccessMessageMixin, AjaxBaseView, UpdateView):
    """Ajax View to update an object and refresh content in partial_template_name."""
    title = _('Updated')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data()
        context['form'] = self.get_form()
        context['object'] = self.get_object()
        context['object_list'] = self.get_object()
        return context


class AjaxDeleteView(SuccessMessageMixin, AjaxBaseView, DeleteView):
    """Ajax View to delete an object and refresh content in partial_template_name."""
    title = _('Deleted')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data()
        context['object'] = self.get_object()
        context['object_list'] = self.get_object()
        return context
