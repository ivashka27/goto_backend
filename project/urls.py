from django.contrib import admin
from django.urls import include, path
from main.views import index

urlpatterns = [
    path('main/', include('main.urls')),
    path('admin/', admin.site.urls),
    path('', index),
]
