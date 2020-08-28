from django.contrib import admin
from .models import (
    UserFacesTraining,
    Attendence_class,
    UserFaceRecognize,
    Attendence_exam
)


admin.site.register(UserFacesTraining)
admin.site.register(Attendence_class)
admin.site.register(UserFaceRecognize)
admin.site.register(Attendence_exam)