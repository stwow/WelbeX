from django.shortcuts import render
from .models import Table
from django.core.paginator import Paginator


def index(request):
    if request.method == 'POST':
        print(request.POST)
        if request.POST['condition'] == 'more' and request.POST['column'] == 'number':    #количество больше
            qs = Table.objects.filter(number__gt = int(request.POST['value']))
        elif request.POST['condition'] == 'more' and request.POST['column'] == 'distance':  #расстояние больше
            qs = Table.objects.filter(distance__gt = int(request.POST['value']))
        elif request.POST['condition'] == 'less' and request.POST['column'] == 'number':   #количество меньше
            qs = Table.objects.filter(number__lt = int(request.POST['value']))
        elif request.POST['condition'] == 'less' and request.POST['column'] == 'distance':#расстояние меньше
            qs = Table.objects.filter(distance__lt = int(request.POST['value']))
        elif request.POST['condition'] == 'more':           #больше- работает на названиях (по алфавиту)
            qs = Table.objects.order_by(request.POST['column'])
        elif request.POST['condition'] == 'less':           #меньше - работает на названиях  (по алфавиту)
            qs = Table.objects.order_by(f"-{request.POST['column']}")
        elif request.POST['condition'] == 'equals' and request.POST['column'] == 'title':           #точное совпадение названия
            qs = Table.objects.raw(f"select * from first_table_table where {request.POST['column']} like '{request.POST['value']}'")
        elif request.POST['condition'] == 'contains' and request.POST['column'] == 'title':            #совпадение названий по входящим словам или буквам
            qs = Table.objects.raw(f"select * from first_table_table where title like '%%{request.POST['value']}%%'")
        elif request.POST['column'] == 'distance' and request.POST['condition'] == 'equals':        #точное расстояние
            qs = Table.objects.filter(distance=int(request.POST['value']))
        elif request.POST['column'] == 'number' and request.POST['condition'] == 'equals':          #точное количество
            qs = Table.objects.filter(number=int(request.POST['value']))
        elif request.POST['column'] == 'number' and request.POST['condition'] == 'contains':    #количество "содержит" (больше либо равно)
            qs = Table.objects.filter(number__gte=int(request.POST['value']))
        elif request.POST['column'] == 'distance' and request.POST['condition'] == 'contains':  #расстояние "содержит" (больше либо равно)
            qs = Table.objects.filter(distance__gte=int(request.POST['value']))
        paginator = Paginator(qs, 4)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        context = {'page_obj': page_obj}
        return render(request, 'first_table/base.html', context)

    qs = Table.objects.all()
    paginator = Paginator(qs, 4)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'page_obj':page_obj}
    return render(request, 'first_table/base.html', context)

