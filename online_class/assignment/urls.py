from django.urls import path, include
from .views import *

# urlpatterns = [
#     path('',assignment_home, name='assignemnt_home'),
#     path('add/',assignment_add, name='assignemnt_add'),
#     path('<')
# ]


urlpatterns = [
    path('teachers/', include(([
        path('', assignment_home, name='assignemnt_home'),
    ],'classromm'), namespace='teachers'))
]
