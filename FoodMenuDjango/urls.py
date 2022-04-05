from django.contrib import admin
from django.urls import include, path
from AppUser import views as user_views
from django.contrib.auth import views as autntication_viwes
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('AppFood.urls')),
    path('register/', user_views.register, name='register'),
    path('login/', autntication_viwes.LoginView.as_view(template_name='user/login.html'), name='login'),
    path('logout/', autntication_viwes.LogoutView.as_view(template_name='user/logout.html'), name='logout'),
    path('profile/', user_views.profilepage, name='profile'),
]



urlpatterns += [
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)