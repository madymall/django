
from django.contrib import admin
from django.urls import path
from main import views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.test),
    path('test1/', views.test1),
    path('test2/', views.test2),
    path('test3/', views.test3)
]
