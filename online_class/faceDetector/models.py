from django.db import models
from django.shortcuts import reverse
from django.conf import settings

from assignment.models import (
    User,
    Student
)
from exam.models import (
    ExamQuestions,
)


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


class UserFaceRecognize(models.Model):
    def user_directory_path(instance, filename):
        return 'faceDetector/recognize/{0}.png'.format(instance.user.id)

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=user_directory_path, blank=True, null=True, verbose_name='Image1')


class Attendence_class(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    class_details = models.ForeignKey('class.Routine', on_delete=models.CASCADE)
    # date = models.DateTimeField(auto_now=True)
    is_present = models.BooleanField(default=False)

    def __str__(self):
        return str(self.class_ + "-" + self.user.username)


class Attendence_exam(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    examQuestions = models.ForeignKey(ExamQuestions, on_delete=models.CASCADE)
    is_present = models.BooleanField(default=False)

    def __str__(self):
        return(self.examQuestions.title + '-' + self.student.user.username)