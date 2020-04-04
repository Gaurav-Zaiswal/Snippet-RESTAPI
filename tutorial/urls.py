from django.contrib import admin
from django.urls import path, include
from django.conf.urls import include

urlpatterns = [
    path('', include('snippets.urls')),
    path('api-auth/', include('rest_framework.urls')),  # this will create login option on the right top, if using post man this url is not required since we can send log in credential manually in postman
]
