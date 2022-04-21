from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path

from . import views

urlpatterns = [
    path('', views.upload_music),
    path('get/', views.get_music),
    path('delete/', views.delete_music),
    path('get_all/', views.get_all_music),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MUSIC_URL, document_root=settings.MUSIC_ROOT)
