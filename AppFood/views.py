from django.shortcuts import render, HttpResponse,redirect
from .models import *
from .forms import *


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


def add(request):
    form = ItemForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('AppFood:index')
    return render(request,'food/add.html',{'form':form})
