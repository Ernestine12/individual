from importlib.resources import path
from myapp import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('detail.html', views.detail, name='detail'),
]