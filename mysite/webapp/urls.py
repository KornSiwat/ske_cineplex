from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.default, name='default'),
    path('home/', views.home, name='home'),
    path('movie/', views.movie, name='movie'),
    path('movie/<int:id>', views.movie_info, name='movie_info'),
    path('booking/<int:id>', views.booking, name='booking'),
    path('update/<int:id>/<str:showtime>', views.update_seat, name='update_seat'),
    path('branches/', views.branches, name='branches'),
    path('contact/', views.contact, name='contact'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
