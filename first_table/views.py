from django.shortcuts import render, redirect
from .models import Table
from django.core.paginator import Paginator


def index(request):
    # if request.method == 'POST':
    #     print(request.POST)
    #     if request.POST['condition'] == 'more':
    #         qs = Table.objects.order_by(request.POST['column'])
    #     elif request.POST['condition'] == 'less':
    #         qs = Table.objects.order_by(f"-{request.POST['column']}")
    #     elif request.POST['condition'] == 'equals' and request.POST['column'] == 'title':
    #         qs = Table.objects.raw(f"select * from first_table_table where {request.POST['column']} like '{request.POST['value']}'")
    #     elif request.POST['condition'] == 'contains' and request.POST['column'] == 'title':
    #         qs = Table.objects.raw(f"select * from first_table_table where title like '%%{request.POST['value']}%%'")
    #     elif request.POST['column'] == 'distance' and request.POST['condition'] == 'equals':
    #         qs = Table.objects.filter(distance=int(request.POST['value']))
    #     elif request.POST['column'] == 'number' and request.POST['condition'] == 'equals':
    #         qs = Table.objects.filter(number=int(request.POST['value']))
    #     elif request.POST['column'] == 'number' and request.POST['condition'] == 'contains':
    #         qs = Table.objects.filter(number__gte=int(request.POST['value']))
    #     elif request.POST['column'] == 'distance' and request.POST['condition'] == 'contains':
    #         qs = Table.objects.filter(distance__gte=int(request.POST['value']))
    #     paginator = Paginator(qs, 4)
    #     page_number = request.GET.get('page')
    #     page_obj = paginator.get_page(page_number)
    #     context = {'page_obj': page_obj}
    #     return render(request, 'first_table/base.html', context)

    qs = Table.objects.all()
    paginator = Paginator(qs, 4)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {'page_obj':page_obj}
    return render(request, 'first_table/base.html', context)


def sort_table(request):
    if request.method == 'POST':
        print(request.POST)
        if request.POST['condition'] == 'more':
            qs = Table.objects.order_by(request.POST['column'])
        elif request.POST['condition'] == 'less':
            qs = Table.objects.order_by(f"-{request.POST['column']}")
        elif request.POST['condition'] == 'equals' and request.POST['column'] == 'title':
            qs = Table.objects.raw(f"select * from first_table_table where {request.POST['column']} like '{request.POST['value']}'")
        elif request.POST['condition'] == 'contains' and request.POST['column'] == 'title':
            qs = Table.objects.raw(f"select * from first_table_table where title like '%%{request.POST['value']}%%'")
        elif request.POST['column'] == 'distance' and request.POST['condition'] == 'equals':
            qs = Table.objects.filter(distance=int(request.POST['value']))
        elif request.POST['column'] == 'number' and request.POST['condition'] == 'equals':
            qs = Table.objects.filter(number=int(request.POST['value']))
        elif request.POST['column'] == 'number' and request.POST['condition'] == 'contains':
            qs = Table.objects.filter(number__gte=int(request.POST['value']))
        elif request.POST['column'] == 'distance' and request.POST['condition'] == 'contains':
            qs = Table.objects.filter(distance__gte=int(request.POST['value']))
        paginator = Paginator(qs, 4)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        context = {'page_obj': page_obj}
        return render(request, 'first_table/base.html', context)