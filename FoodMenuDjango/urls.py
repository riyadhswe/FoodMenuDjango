from django.contrib import admin
from django.urls import include, path
from AppUser import views as user_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('AppFood.urls')),
    path('register/', user_views.register, name='register'),
]
