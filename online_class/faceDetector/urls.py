from django.urls import path
from .views import (
    attendence_class,
    attendence_exam,
    train_model,
    add_images,
    redirection
)

urlpatterns = [
    path('face-recognition/attendece/class/', attendence_class, name="attendence_class"),
    path('face-recognition/attedence/exam<int:id>/', attendence_exam, name="attendence_exam"),
    path('face-recognition/train/', train_model, name="train-model"),
    path('face-recognition/add-images/', add_images, name="add-images"),
    path('redirection/', redirection, name='redirect-name')
]