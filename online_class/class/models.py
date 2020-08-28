from django.db import models


class Class(models.Model):
    class_name = models.CharField(verbose_name="Name of Subject", max_length = 100)
    teacher_name = models.CharField(verbose_name="Name of Teacher", max_length = 100)
    sem = models.PositiveIntegerField(verbose_name="Semister")
    course_time = models.PositiveIntegerField(verbose_name="Total study Hour")

    def __str__(self):
        return str(self.class_name)
    
    

class Routine(models.Model):
    day = models.PositiveIntegerField(verbose_name="Day of week in integer")
    class_name = models.ForeignKey("class.Class", on_delete=models.CASCADE, verbose_name="Subject Name")
    start_time = models.TimeField(verbose_name="Class start time")
    end_time = models.TimeField(verbose_name="Class end time")

    def __str__(self):

        day_name = ""
        if day == 1:
            day_name = "Sunday"
        elif day == 2:
            day_name = "Monday"
        elif day == 3:
            day_name = "Tuesday"
        elif day == 4:
            day_name = "Wednesday"
        elif day == 5:
            day_name = "Thursday"
        elif day == 6:
            day_name = "Friday"
        else:
            day_name == "Saturday"

        return day_name + str(class_name) 
    