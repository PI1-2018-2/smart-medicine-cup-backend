from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('landing_page.urls')),
    path('api/', include('smc.urls')),
    path('dashboard/', include('dashboard.urls')),
]
