from django.db import models

from assignment.models import (
    User,
    Student,
)


class ExamQuestions(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    title = models.CharField(max_length=225)
    # subject = models.ForeignKey('class.Class', on_delete=models.CASCADE)
    exam_date = models.DateField("Submission Date")

    question1 = models.TextField('Question 1', default="Add Question", null=True)
    question1_total_marks = models.PositiveIntegerField(null=True)

    question2 = models.TextField('Question 2', default="Add Question", null=True)
    question2_total_marks = models.PositiveIntegerField(null=True)

    question3 = models.TextField('Question 3', default="Add Question", null=True)
    question3_total_marks = models.PositiveIntegerField(null=True)

    full_marks = models.PositiveIntegerField()

    def __str__(self):
        return str(self.owner.username + "-" + self.title)


class ExamAnswers(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='exam_answer')
    examQuestions = models.ForeignKey(ExamQuestions, on_delete=models.CASCADE)

    question1_answer = models.TextField('Question 1 Answer', default="Add Question", null=True)
    question1_marks = models.PositiveIntegerField(null=True)

    question2_answer = models.TextField('Question 2 Answer', default="Add Question", null=True)
    question2_marks = models.PositiveIntegerField(null=True)

    question3_answer = models.TextField('Question 3 Answer', default="Add Question", null=True)
    question3_marks = models.PositiveIntegerField(null=True)

    total_marks_obtained = models.PositiveIntegerField(null=True)

    def __str__(self):
        return(self.ExamQuestions.title + '-' + self.student.user)

