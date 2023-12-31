"""Ajax helpers views."""

# Django
from django.contrib.messages.views import SuccessMessageMixin
from django.core.exceptions import ObjectDoesNotExist
from django.core.paginator import Paginator
from django.utils.translation import gettext_lazy as _
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.views import View
from django.views.generic import CreateView
from django.views.generic import DeleteView
from django.views.generic import DetailView
from django.views.generic import UpdateView


class AjaxBaseView(SuccessMessageMixin, View):
    """Ajax base view."""

    template_name = None
    partial_template_name = None
    model = None
    title = None
    paginate_by = 2  # Should be the same as in the current model's list view.

    def get_queryset(self):  # noqa: D102
        return self.model.objects.all()

    def get_context_data(self, *args, **kwargs):  # noqa: D102
        return {}

    def json_response(self, status, template, form=None, message=None, title=None, page=None):
        """Return JsonResponse wih custom values."""
        context = self.get_context_data()
        if form:
            context['form'] = form
        if page:
            context['object_list'] = page.object_list
            context['page_obj'] = page
        return JsonResponse({
            'html': render_to_string(
                template,
                context,
                self.request,
            ),
            'message': message,
            'title': title,
        }, status=status)

    def get(self, request, *args, **kwargs):  # noqa: D102
        return self.json_response(
            status=200,
            template=self.template_name,
        )

    def form_valid(self, form):  # noqa: D102
        form.save()
        page_number = self.request.POST.get('page', 1)
        paginator = Paginator(self.get_queryset(), self.paginate_by)
        page = paginator.get_page(page_number)
        return self.json_response(
            status=200,
            template=self.partial_template_name,
            message=self.success_message,
            title=self.title,
            page=page,
        )

    def form_invalid(self, form):  # noqa: D102
        return self.json_response(
            status=400,
            template=self.template_name,
            form=form,
        )


class AjaxDetailView(AjaxBaseView, DetailView):
    """Ajax View to show detail of an object."""

    def get_queryset(self):  # noqa: D102
        return self.model.objects.all()

    def get_context_data(self, *args, **kwargs):  # noqa: D102
        context = super().get_context_data()
        context['object'] = self.get_object()
        return context


class AjaxCreateView(AjaxBaseView, CreateView):
    """Ajax View to create an object and refresh content in partial_template_name."""

    success_message = _('Object was successfully created')
    title = _('Created')

    def get_context_data(self, *args, **kwargs):  # noqa: D102
        context = super().get_context_data()
        context['form'] = self.get_form()
        context['object_list'] = self.get_queryset()
        return context


class AjaxUpdateView(AjaxBaseView, UpdateView):
    """Ajax View to update an object and refresh content in partial_template_name."""

    success_message = _('Object was successfully updated')
    title = _('Updated')

    def get_context_data(self, *args, **kwargs):  # noqa: D102
        context = super().get_context_data()
        context['form'] = self.form_class(instance=self.get_object())
        context['object'] = self.get_object()
        context['object_list'] = self.get_queryset()
        return context


class AjaxDeleteView(AjaxBaseView, DeleteView):
    """Ajax View to delete an object and refresh content in partial_template_name."""

    success_message = _('Object was successfully deleted')
    title = _('Deleted')

    def get_context_data(self, *args, **kwargs):  # noqa: D102
        context = super().get_context_data()
        try:
            context['object'] = self.model.objects.get(pk=self.kwargs.get('pk'))
        except ObjectDoesNotExist:
            pass
        context['object_list'] = self.get_queryset()
        return context

    def form_valid(self, request, *args, **kwargs):  # noqa: D102
        self.get_object().delete()
        return self.json_response(
            status=200,
            template=self.partial_template_name,
            message=self.success_message,
            title=self.title,
        )
