from django.urls import path
from . import views

urlpatterns = [
    path('', views.class_view, name="class_page"),
]