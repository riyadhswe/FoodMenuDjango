from . import views
from django.urls import path

app_name = 'AppFood'
urlpatterns = [
    path('', views.IndexClassView.as_view(), name='index'),
    path('<int:pk>', views.FoodDetail.as_view(), name='detail'),
    path('item/', views.item, name='item'),

    # add items
    path('add/', views.CreateItem.as_view(), name='add'),
    # update items
    path('edit/<int:id>/', views.edit, name='edit'),
    # delete items
    path('delete/<int:id>/', views.delete, name='delete')
]