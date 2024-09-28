from django.contrib import admin
from django.urls import path
from users.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),  # Set the home view for the root URL
]
