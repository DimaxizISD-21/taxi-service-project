from django.urls import path
from accounts.views import (
    DispatcherLoginView,
    DispatcherProfileView,
    DispatcherRegisterView,
    DispatcherLogoutView,
    RemoveTaxiOrder
)

app_name = 'dispatcher'

urlpatterns = [
    path('dispatcher_login/', DispatcherLoginView.as_view(), name='dispatcher_login'),
    path('dispatcher_logout/', DispatcherLogoutView.as_view(), name='dispatcher_logout'),
    path('dispatcher_register/', DispatcherRegisterView.as_view(), name='dispatcher_register'),
    path('dispatcher_profile/', DispatcherProfileView.as_view(), name='dispatcher_profile'),
    path('dispatcher_profile/remove_order/<int:order_id>/', RemoveTaxiOrder.as_view(), name='remove_order'),
]