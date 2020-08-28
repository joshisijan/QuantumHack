from django.urls import path, include
from .views import *

# urlpatterns = [
#     path('',assignment_home, name='assignment_page'),
#     path('add/',assignment_add, name='assignment_add'),
# ]


urlpatterns = [
    path('', home, name='home'),
    
    path('teachers/', include(([
        path('', assignment_home, name='assignment_page'),
        path('assignment/add/', assignment_add, name='assignment_add'),
        path('assignment/<int:pk>/', assignment_update, name='assignment_update'),
        path('assignment/<int:pk>/delete/', assignment_delete, name='assignment_delete'),
    ],'assignment'), namespace='teachers')),

    path('students/', include(([
        path('', student_assignment_home, name='assignment_page'),
    ],'assignment'), namespace='students'))

]
