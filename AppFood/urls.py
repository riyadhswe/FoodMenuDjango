from . import views
from django.urls import path

app_name = 'AppFood'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:item_id>', views.detail, name='detail'),
    path('item/', views.item, name='item'),

    # add items
    path('add/', views.add, name='add'),
    # update items
    path('edit/<int:id>/', views.edit, name='edit'),
    # delete items
    path('delete/<int:id>/', views.delete, name='delete')
]
