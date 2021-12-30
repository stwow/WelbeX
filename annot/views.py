from django.db.models import Sum,Count
from django.http import HttpResponse
from django.shortcuts import render
from .models import Task,TaskOnTime,Project


def main(request, pk):
    qs = Task.objects.filter(project_id=pk).annotate(total_working_time = Count('taskontime__time'))
    print(list(qs))
    print(vars(qs[0]))
    print(qs[0].total_working_time)
    return HttpResponse(qs[0])