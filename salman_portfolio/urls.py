
from django.contrib import admin
from django.urls import path
from application.views import home,about,contact,showdata

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', home , name='home'),
    path('about/', about , name='about'),
    path('contact/', contact , name='contact'),
    path('showdata/', showdata , name='showdata'),
]
