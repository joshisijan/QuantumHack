from django.urls import path
from . import views

urlpatterns = [
    path('', views.exam_view, name="exam_page"),
]