from django.urls import path
from .views import get_stripe_session_id, get_info_about_item, success, cancel, all_obj

urlpatterns = [

    path('buy/<int:id>', get_stripe_session_id,  name='create-checkout-session'),
    path('item/<int:id>', get_info_about_item, name='item'),
    path('cancel/', cancel, name='cancel'),
    path('success/', success, name='success'),
    path('', all_obj, name='home')
               ]
