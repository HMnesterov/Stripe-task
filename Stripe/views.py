from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, get_object_or_404
import stripe

import config.settings
from Stripe.models import Item

stripe.api_key = config.settings.STRIPE_SECRET_KEY
public_key = config.settings.STRIPE_PUBLISHABLE_KEY


def get_stripe_session_id(request, id):
    '''Получение id сессии'''
    item = get_object_or_404(Item, id=id)

    session = stripe.checkout.Session.create(
        line_items=[
            {
                "price_data": {
                    "currency": "usd",
                    "product_data": {"name": item.name},
                    "unit_amount": item.price,
                },
                "quantity": 1,
            },
        ],
        mode="payment",
        success_url=config.settings.DOMAIN + '/success/',
        cancel_url=config.settings.DOMAIN + '/cancel/'
    )


    return JsonResponse({'sessionId': session.id})


def get_info_about_item(request, id):
    '''Выдаёт данные продукта, кнопку для оплаты'''
    item = get_object_or_404(Item, id=id)
    return render(request, 'stripe/checkout.html', {'item': item, 'public_key': public_key})


def success(request):
    return HttpResponse('Успешно')


def cancel(request):
    return HttpResponse("No, that's wrong!")


def all_obj(request):
    items = Item.objects.all()

    return render(request, 'stripe/items.html', {'items': items})
