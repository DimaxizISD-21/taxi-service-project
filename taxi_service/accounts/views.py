from django.contrib.auth import get_user_model, authenticate, login, logout
from django.shortcuts import redirect
from django.views.generic import TemplateView, ListView, FormView, View
from accounts.forms import DispatcherLoginForm, DispatcherRegistrationForm

from taxi.models import TaxiOrder, TaxiAuto

# Create your views here.

User = get_user_model()

class DispatcherLoginView(TemplateView, FormView):
    template_name = 'dispatcher_login.html'
    form_class = DispatcherLoginForm

    def form_valid(self, form):
        data = form.cleaned_data
        dispatcher = authenticate(self.request, **data)
        login(self.request, dispatcher)
        return redirect('dispatcher:dispatcher_profile')


class DispatcherRegisterView(TemplateView, FormView):
    template_name = 'dispatcher_register.html'
    form_class = DispatcherRegistrationForm

    def form_valid(self, form):
        new_user = form.save(commit=False)
        new_user.set_password(form.cleaned_data['password'])
        new_user.save()
        return redirect('dispatcher:dispatcher_login')


class DispatcherLogoutView(View):

    def get(self, *args):
        logout(self.request)
        return redirect('taxi:home')


class DispatcherProfileView(ListView):
    template_name = 'dispatcher_profile.html'
    context_object_name = 'taxi_orders_list'
    paginate_by = 3

    def get_queryset(self):
        qs = TaxiOrder.objects.all()
        return qs


class RemoveTaxiOrder(View):

    def post(self, request, order_id):
        get_taxi_auto = TaxiAuto.objects.get(taxiorder=order_id)
        get_taxi_auto.taxi_status = 'free'
        get_taxi_auto.save()
        TaxiOrder.objects.filter(id__lte=order_id).delete()
        return redirect('dispatcher:dispatcher_profile')
