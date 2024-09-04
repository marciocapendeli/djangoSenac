
from django.contrib import admin
from django.urls import path
from usuarios import views as usuarios_views
from porteiros import views as porteiros_views
from visitantes import views as visitantes_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('usuarios/', usuarios_views.index, name='usuarios_index'),
    path('porteiros/', porteiros_views.index, name='porteiros_index'),
    path('visitantes/', visitantes_views.index, name='visitantes_index'),
]
