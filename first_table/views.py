from django.shortcuts import render
from .models import Table
from django.core.paginator import Paginator


def index(request):
    qs = Table.objects.all()
    paginator = Paginator(qs, 4)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'page_obj': page_obj}
    return render(request, 'first_table/base.html', context)


def sorts(request):
    qs = Table.objects.all()
    if request.method == 'POST':
        if request.POST['condition'] == 'more' and not request.POST['value'] and request.POST[
            'column'] == 'title':  # название - больше (по алфавиту)
            result = qs.order_by(request.POST['column'])
        elif request.POST['condition'] == 'less' and not request.POST['value'] and request.POST[
            'column'] == 'title':  # название - меньше (по алфавиту)
            result = qs.order_by(f"-{request.POST['column']}")
        elif request.POST['condition'] == 'more' and request.POST['column'] == 'number' and request.POST[
            'value']:  # количество больше
            result = qs.filter(number__gt=int(request.POST['value']))
        elif request.POST['condition'] == 'more' and request.POST['column'] == 'distance' and request.POST[
            'value']:  # расстояние больше
            result = qs.filter(distance__gt=int(request.POST['value']))
        elif request.POST['condition'] == 'less' and request.POST['column'] == 'number' and request.POST[
            'value']:  # количество меньше
            result = qs.filter(number__lt=int(request.POST['value']))
        elif request.POST['condition'] == 'less' and request.POST['column'] == 'distance' and request.POST[
            'value']:  # расстояние меньше
            result = qs.filter(distance__lt=int(request.POST['value']))
        elif request.POST['condition'] == 'equals' and request.POST['column'] == 'title':  # название - равно
            result = qs.filter(title__iexact=request.POST['value'])
        elif request.POST['condition'] == 'contains' and request.POST['column'] == 'title':  # название - содержит
            result = qs.filter(title__icontains=request.POST['value'])
        elif request.POST['column'] == 'distance' and request.POST['condition'] == 'equals' and request.POST[
            'value']:  # расстояние - равно
            result = qs.filter(distance=int(request.POST['value']))
        elif request.POST['column'] == 'number' and request.POST['condition'] == 'equals' and request.POST[
            'value']:  # количество - равно
            result = qs.filter(number=int(request.POST['value']))
        elif request.POST['column'] == 'number' and request.POST['condition'] == 'contains' and request.POST[
            'value']:  # количество "содержит" (больше либо равно)
            result = qs.filter(number__gte=int(request.POST['value']))
        elif request.POST['column'] == 'distance' and request.POST['condition'] == 'contains' and request.POST[
            'value']:  # расстояние "содержит" (больше либо равно)
            result = qs.filter(distance__gte=int(request.POST['value']))
        else:
            result = qs.all()

        paginator = Paginator(result, 4)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        context = {'page_obj': page_obj}

        return render(request, 'first_table/sort.html', context)