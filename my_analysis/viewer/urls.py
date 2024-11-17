from django.urls import path
from . import views

urlpatterns = [
    path('notebook/', views.notebook_results_view, name='notebook_results'),
]
