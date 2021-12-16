from django.shortcuts import render
from .models import Table
from django.core.paginator import Paginator

qs = Table.objects.all()



def index(request):
    paginator = Paginator(qs, 4)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'page_obj': page_obj}
    return render(request, 'first_table/base.html', context)


def sorts(request):
    global qs
    if request.method == 'POST':
        if request.POST['condition'] == 'more':                                 # значение больше
            if not request.POST['value']:
                qs = qs.order_by(request.POST['column'])                    # название - больше (по алфавиту)
            elif request.POST['value'] and request.POST['column'] == 'number':
                qs = qs.filter(number__gt=int(request.POST['value']))       # количество больше
            elif request.POST['value'] and request.POST['column'] == 'distance':
                qs = qs.filter(distance__gt=int(request.POST['value']))      # расстояние больше
        elif request.POST['condition'] == 'less':                                # значение меньше
            if not request.POST['value']:
                qs = qs.order_by(f"-{request.POST['column']}")               # название - меньше (по алфавиту)
            elif request.POST['value'] and request.POST['column'] == 'number':
                qs = qs.filter(number__lt=int(request.POST['value']))       # количество меньше
            elif request.POST['value'] and request.POST['column'] == 'distance':
                qs = qs.filter(distance__lt=int(request.POST['value']))     # расстояние меньше
        elif request.POST['condition'] == 'contains':                            # значение содержит
            if request.POST['column'] == 'title':
                qs = qs.filter(title__icontains=request.POST['value'])      # название содержит
            elif request.POST['column'] == 'number' and request.POST['value']:
                qs = qs.filter(number__gte=int(request.POST['value']))       # количество "содержит" (больше либо равно)
            elif request.POST['column'] == 'distance' and request.POST['value']:
                qs = qs.filter(distance__gte=int(request.POST['value']))     # расстояние "содержит" (больше либо равно)
        elif request.POST['condition'] == 'equals':                              # значение равно
            if request.POST['column'] == 'title':
                qs = qs.filter(title__iexact=request.POST['value'])          # название равно
            elif request.POST['column'] == 'number' and request.POST['value']:
                qs = qs.filter(number=int(request.POST['value']))            # количество равно
            elif request.POST['column'] == 'distance' and request.POST['value']:
                qs = qs.filter(distance=int(request.POST['value']))           # расстояние равно
        else:
            qs = qs.all()

    paginator = Paginator(qs, 4)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'page_obj': page_obj}
    return render(request, 'first_table/sort.html', context)
