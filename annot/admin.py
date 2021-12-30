from django.contrib import admin
from .models import Task,TaskOnTime,Project


admin.site.register(Task)
admin.site.register(TaskOnTime)
admin.site.register(Project)
# Register your models here.
