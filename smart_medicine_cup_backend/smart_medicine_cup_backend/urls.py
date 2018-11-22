from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('landing_page.urls')),
    path('dashboard/', include('dashboard.urls')),
    path('user/', include('user.urls')),
]
