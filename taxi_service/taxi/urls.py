from django.urls import path
from taxi.views import HomeView, OrderSuccessView, OrderDetailView

app_name = 'taxi'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('order_success/', OrderSuccessView.as_view(), name='order_success'),
    path('dispatcher/dispatcher_profile/order_detail/<int:pk>/', OrderDetailView.as_view(), name='order_detail'),
]