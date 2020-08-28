from django.contrib import admin

from . import models

# Register your models here.

admin.site.register(models.Class)
admin.site.register(models.Routine)
admin.site.regisster(models.Teacher)