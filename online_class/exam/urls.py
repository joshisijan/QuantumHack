from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.exam_view, name="exam_page"),

    # path('teachers/', include(([
    #     path('', exam_home, name='exam_page'),
    #     path('exam/add/', exam_add, name='exam_add'),
    #     path('exam/<int:pk>/', exam_update, name='exam_update'),
    #     path('exam/<int:pk>/delete/', exam_delete, name='exam_delete'),
    # ],'exam'), namespace='teachers')),
]