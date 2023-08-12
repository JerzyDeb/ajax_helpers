"""Core urls."""

# Django
from django.urls import path

# Local
from .views import IndexView
from .views import TestModelCreateView
from .views import TestModelDeleteView
from .views import TestModelDetailView
from .views import TestModelUpdateView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('create/', TestModelCreateView.as_view(), name='create'),
    path('detail/<int:pk>/', TestModelDetailView.as_view(), name='detail'),
    path('update/<int:pk>/', TestModelUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', TestModelDeleteView.as_view(), name='delete'),
]
