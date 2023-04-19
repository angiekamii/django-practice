from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', views.hello),
    path('number/', views.evenodd),
    path('index/', views.index),
    path('var/', views.variables),
    path('ass/', views.assignment),
    path('images/', views.images),
    path('background/', views.background),
    path('memebers/', views.members),
    path('student/', views.student),
    path('employee/', views.employee),
    path('session/', views.getsession),
    path('form/', views.form),
    path('', views.company),

]
