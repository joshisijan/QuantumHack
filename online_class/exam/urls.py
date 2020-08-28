from django.urls import path
from . import views

urlpatterns = [
    path('exam/', views.exam_view, name="exam_page"),
]