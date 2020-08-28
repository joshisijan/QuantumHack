from django.contrib import admin
from .models import (
    UserFacesTraining,
    Attendence_class,
    UserFaceRecognize
)


admin.site.register(UserFacesTraining)
admin.site.register(Attendence_class)
admin.site.register(UserFaceRecognize)