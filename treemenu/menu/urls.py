from django.urls import path
from .views import index
urlpatterns = [
    path('main', index,{'title':'Главная страница'}, name='main'),
    path('about', index,{'title':'О нас'} ,name='main'),
    path('about/history', index,{'title':'Наша история развития'}, name='main'),
]
