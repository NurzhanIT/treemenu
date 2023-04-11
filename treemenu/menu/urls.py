from django.urls import path
from .views import index

urlpatterns = [
    path('main', index, {'title': 'Главная страница ...'}, name='main'),
    path('about', index, {'title': 'О нас ...'}, name='main'),
    path('about/history', index, {'title': 'Наша история развития ...'}, name='main'),
    path('about/services', index, {'title': 'Наши услуги ...'}, name='main'),
    path('about/contacts', index, {'title': 'Наши контакты ...'}, name='main'),
    path('prices', index, {'title': 'Цены на услуги ...'}, name='main'),
    path('prices/promotion', index, {'title': 'Акции ...'}, name='main'),
    path('prices/sales', index, {'title': 'Скидки %%%'}, name='main'),
    path('prices/sales/for-students', index, {'title': 'Для студентов ...'}, name='main'),
    path('prices/sales/for-pensioners', index, {'title': 'Для пенисонеров ...'}, name='main'),
    path('partners', index, {'title': 'Партнеры ...'}, name='main'),
]
