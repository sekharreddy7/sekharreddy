from django.contrib import admin
from django.urls import path
app_name='app1'
from app1 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('app1/',views.dhoni,name='app1'),
]
