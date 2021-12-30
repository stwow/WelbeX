from django.db import models

class TaskOnTime(models.Model):
    task = models.ForeignKey('Task', on_delete=models.CASCADE)
    time = models.DateTimeField()
    title = models.CharField(max_length=25)


class Task(models.Model):
    title = models.CharField(max_length=25)
    start = models.CharField(max_length=25)
    project = models.ForeignKey('Project', on_delete=models.CASCADE)


class Project(models.Model):
    title = models.CharField(max_length=25)

