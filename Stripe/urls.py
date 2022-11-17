from django.urls import path
from .views import get_stripe_session_id, get_info_about_item, success, cancel

urlpatterns = [

    path('buy/<int:pk>', get_stripe_session_id,  name='create-checkout-session'),
    path('item/<int:pk>', get_info_about_item),
    path('cancel/', cancel, name='cancel'),
    path('success/', success, name='success'),
               ]
