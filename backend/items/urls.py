from django.urls import path

from .views import buy_item, get_item, success, order, buy_order, index

app_name = 'items'

urlpatterns = [
    path('', index, name='index'),
    path('buy/<item_id>/', buy_item, name='buy_item'),
    path('buy_order/', buy_order, name='buy_order'),
    path('item/<item_id>/', get_item, name='get_item'),
    path('order/', order, name='order'),
    path('success/', success, name='success'),
    path('cancelled/', success, name='cancelled'),
]
