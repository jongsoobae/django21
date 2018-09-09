from django.db import models


class School(models.Model):
    name = models.CharField(max_length=100)

    objects = models.Manager()

class Classs(models.Model):
    name = models.CharField(max_length=100)
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    grade = models.PositiveSmallIntegerField()

    objects = models.Manager()

    def __str__(self):
        return '{}: {}'.format(self.school.name, self.name)


class Student(models.Model):
    name = models.CharField(max_length=100)
    classs = models.ForeignKey(Classs, on_delete=models.CASCADE)

    objects = models.Manager()
