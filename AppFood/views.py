from django.shortcuts import render, HttpResponse
from .models import *


# Create your views here.
def index(request):
    item_list = Item.objects.all()
    contex = {
        'item_list': item_list,
    }
    return render(request, 'food/index.html', contex)


def item(request):
    return HttpResponse('This is an item')


def detail(request, item_id):
    item = Item.objects.get(pk=item_id)
    context = {
        'item': item,
    }
    return render(request, 'food/detail.html', context)
