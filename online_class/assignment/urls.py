from django.urls import path
from . import views

urlpatterns = [
    path('assignment/', views.assignment_view, name="assignment_page"),
]