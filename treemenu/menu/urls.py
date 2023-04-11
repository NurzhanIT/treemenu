from django.urls import path
from .views import index

urlpatterns = [
    path('main', index, {'title': 'Главная страница ...'}, name='main'),
    path('about', index, {'title': 'О нас ...'}, name='about'),
    path('about/history', index, {'title': 'Наша история развития ...'}, name='about/history'),
    path('about/services', index, {'title': 'Наши услуги ...'}, name='about/services'),
    path('about/contacts', index, {'title': 'Наши контакты ...'}, name='about/contacts'),
    path('prices', index, {'title': 'Цены на услуги ...'}, name='prices'),
    path('prices/promotion', index, {'title': 'Акции ...'}, name='prices/promotion'),
    path('prices/sales', index, {'title': 'Скидки %%%'}, name='prices/sales'),
    path('prices/sales/for-students', index, {'title': 'Для студентов ...'}, name='prices/sales/for-students'),
    path('prices/sales/for-pensioners', index, {'title': 'Для пенисонеров ...'}, name='prices/sales/for-pensioners'),
    path('partners', index, {'title': 'Партнеры ...'}, name='partners'),
]
