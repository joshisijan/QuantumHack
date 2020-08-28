from django.db import models
from django.shortcuts import reverse
from django.conf import settings

from assignment.models import User


class UserFacesTraining(models.Model):
    def user_directory_path(instance, filename):
        return 'faceDetector/dataset/{0}/{1}'.format(instance.user.id, filename)

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image1 = models.ImageField(upload_to=user_directory_path, blank=True, null=True, verbose_name='Image1')
    image2 = models.ImageField(upload_to=user_directory_path, blank=True, null=True, verbose_name='Image2')
    image3 = models.ImageField(upload_to=user_directory_path, blank=True, null=True, verbose_name='Image3')
    image4 = models.ImageField(upload_to=user_directory_path, blank=True, null=True, verbose_name='Image4')
    image5 = models.ImageField(upload_to=user_directory_path, blank=True, null=True, verbose_name='Image5')

    def __str__(self):
        return str(self.user)


class Attendence_class(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    class_details = models.ForeignKey('class.Class', on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now=True)
    is_present = models.BooleanField(default=False)

    def __str__(self):
        return str(self.class_ + "-" + self.user)
