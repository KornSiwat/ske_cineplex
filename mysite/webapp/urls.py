from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.default, name='default'),
    path('home/', views.home, name='home'),
    path('movie/', views.movie, name='movie'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
