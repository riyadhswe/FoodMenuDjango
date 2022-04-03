from django.shortcuts import render, HttpResponse, redirect
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
    return render(request, 'food/add.html', {'form': form})


def edit(request, id):
    item = Item.objects.get(id=id)
    form = ItemForm(request.POST or None, instance=item)
    if form.is_valid():
        form.save()
        return redirect('AppFood:index')

    return render(request, 'food/add.html', {'form': form, 'item': item})


def delete(request, id):
    item = Item.objects.get(id=id)
    if request.method == 'POST':
        item.delete()
        return redirect('AppFood:index')

    return render(request, 'food/delete.html', {'item': item})
