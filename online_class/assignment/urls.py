from django.urls import path, include
from .views import *

# urlpatterns = [
#     path('',assignment_home, name='assignment_page'),
#     path('add/',assignment_add, name='assignment_add'),
# ]


urlpatterns = [
    path('teachers/', include(([
        path('', assignment_home, name='assignment_page'),
    ],'assignment'), namespace='teachers')),

    path('students/', include(([
        path('', assignment_home, name='assignment_page'),
    ],'assignment'), namespace='students'))

]
