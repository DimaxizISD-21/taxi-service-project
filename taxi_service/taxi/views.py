from django.shortcuts import redirect
from django.views.generic import TemplateView, FormView, ListView
from taxi.forms import TaxiOrderForm
from taxi.models import TaxiOrder, TaxiAuto

# Create your views here.

class HomeView(TemplateView, FormView):
    template_name = 'home.html'
    form_class = TaxiOrderForm

    def form_valid(self, form):
        data = form.cleaned_data
        get_taxi_auto = TaxiAuto.objects.get(model_name=data['taxi_auto'])
        get_taxi_auto.taxi_status = 'busy'
        order_taxi = TaxiOrder(**data)
        order_taxi.save()
        get_taxi_auto.save()
        return redirect('taxi:order_success')


class OrderSuccessView(ListView):
    template_name = 'order_success.html'
    context_object_name = 'taxi_orders_list'

    def get_queryset(self):
        qs = TaxiOrder.objects.order_by('-id')[0]
        return qs

