from django.contrib import admin
from django.shortcuts import redirect
from django.urls import path, include

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('auth/', include('authentication.urls')),
    path('tasks/', include('platform_app.urls')),
    path('usuario/', include('usuario.urls')),
    path('', include('authentication.urls'))
]
