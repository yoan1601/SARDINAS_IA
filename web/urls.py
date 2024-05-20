from django.urls import path # type: ignore
from . import views

urlpatterns = [
    path("form/", views.form, name='form'),
    path("submit_view/", views.submit_view, name='submit_view'),
]
