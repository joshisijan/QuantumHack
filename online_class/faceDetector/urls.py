from django.urls import path
from .views import (
    attendence_class,
    attendence_exam,
    train_model,
    add_images,
    redirection,
    # AddImagesView
)

urlpatterns = [
    path('attendence/class/', attendence_class, name="attendence_class"),
    path('attedennce/exam<int:id>/', attendence_exam, name="attendence_exam"),
    path('train/', train_model, name="train-model"),
    path('add-images/', add_images, name="add_images"),
    # path('add-images/', AddImagesView.as_view(), name="add-images"),
    path('redirection/', redirection, name='redirect_name')
]