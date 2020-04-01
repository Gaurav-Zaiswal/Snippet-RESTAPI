from django.contrib import admin
from django.urls import path, include
from django.conf.urls import include

urlpatterns = [
    path('', include('snippets.urls')),
    path('api-auth/', include('rest_framework.urls')),
]
