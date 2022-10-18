from django.urls import path
from .views import view_form

urlpatterns = [
    path('<str:num_form>', view_form),
]
