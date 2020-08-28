from django.urls import path, include
from .views import *

urlpatterns = [
<<<<<<< Updated upstream
    path('',assignment_home, name='assignment_page'),
    path('add/',assignment_add, name='assignment_add'),
=======
    path('', assignment_home, name='assignment_home'),
>>>>>>> Stashed changes
]


# urlpatterns = [
#     path('teachers/', include(([
#         path('', assignment_home, name='assignemnt_home'),
#     ],'assignment'), namespace='teachers'))
# ]
