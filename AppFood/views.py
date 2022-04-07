from django.shortcuts import render, HttpResponse, redirect
from .models import *
from .forms import *
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView

# Create your views here.
"""def index(request):
    item_list = Item.objects.all()
    contex = {
        'item_list': item_list,
    }
    return render(request, 'food/index.html', contex)
"""


class IndexClassView(ListView):
    model = Item
    template_name = 'food/index.html'
    context_object_name = 'item_list'


def item(request):
    return HttpResponse('This is an item')


"""def detail(request, item_id):
    item = Item.objects.get(pk=item_id)
    context = {
        'item': item,
    }
    return render(request, 'food/detail.html', context)
"""


class FoodDetail(DetailView):
    model = Item
    template_name = 'food/detail.html'


"""def add(request):
    form = ItemForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('AppFood:index')
    return render(request, 'food/add.html', {'form': form})
"""


class CreateItem(CreateView):
    model = Item
    fields = ['item_name','item_desc','item_price','item_image']
    template_name = 'food/add.html'

    def form_valid(self, form):
        form.instance.user_name = self.request.user
        return super().form_valid(form)


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
