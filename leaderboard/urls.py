from django.contrib import admin
from django.urls import path, include
from django.conf import settings

if settings.COUNTDOWN_MODE:
    urlpatterns = [
        path('admin/', admin.site.urls),
        path('', include('countdown.urls'))
    ]
else:
    urlpatterns = [
        path('admin/', admin.site.urls),
        path('', include('web.urls'))
    ]
