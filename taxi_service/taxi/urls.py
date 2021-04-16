from django.urls import path
from taxi.views import HomeView, OrderSuccessView

app_name = 'taxi'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('order_success/', OrderSuccessView.as_view(), name='order_success'),
]