import stripe
from django.shortcuts import render
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse
from django.conf import settings

from items.models import Item, Order, Coupon


def buy_item(request, item_id):
    stripe.api_key = settings.STRIPE_SECRET_KEY_TEST
    item = get_object_or_404(Item, id=item_id)
    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[
            {'price': item.price,
             'quantity': 1, },
             ],
        mode='payment',
        success_url=settings.BASE_URL + '/' + reverse('items:success'),
        cancel_url=settings.BASE_URL + '/' + reverse('items:cancelled'), )
    return redirect(session.url, code=303)


def buy_order(request):
    stripe.api_key = settings.STRIPE_SECRET_KEY_TEST
    items = Order.objects.all().prefetch_related('item')
    items_list = []
    for item in items:
        items_list.append({
            'price': item.item.price,
            'quantity': item.quantity, })
    discounts = []
    if Coupon.objects.filter(user=1):
        discounts.append(
            {'coupon': Coupon.objects.filter(user=1).first().coupon_id}
            )
    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=items_list,
        mode='payment',
        success_url=settings.BASE_URL + '/' + reverse('items:success'),
        cancel_url=settings.BASE_URL + '/' + reverse('items:cancelled'),
        discounts=discounts,)
    return redirect(session.url, code=303)


def get_item(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    context = {'item': item}
    return render(request, 'item.html', context=context)


def success(request):
    return render(request, 'success.html')


def cancelled(request):
    return render(request, 'cancelled.html')


def order(request):
    items = Order.objects.all().prefetch_related('item')
    context = {'items': items}
    return render(request, 'order.html', context=context)


def index(request):
    items = Item.objects.all()
    context = {'items': items}
    return render(request, 'index.html', context=context)
