from django.urls import path
from .views import car_price_predict,car_price_result

urlpatterns = [
    path('', car_price_predict, name='car_price_predict'),
    path('', car_price_predict, name='car_price_predict'),
    path('result/', car_price_result, name='car_price_result'),
]
