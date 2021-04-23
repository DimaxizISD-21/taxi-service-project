from django.shortcuts import redirect
from django.contrib import messages
from django.views.generic import TemplateView, FormView, ListView, DetailView
from taxi.forms import TaxiOrderForm
from taxi.models import TaxiOrder, TaxiAuto

# Create your views here.

class HomeView(TemplateView, FormView):
    template_name = 'home.html'
    form_class = TaxiOrderForm

    def form_valid(self, form):
        data = form.cleaned_data
        client_name = data.get('client_name')
        phone_number = data.get('phone_number')
        address = data.get('address')
        desired_time = data.get('desired_time')
        get_taxi_auto = TaxiAuto.objects.filter(taxi_status=True).first()

        if get_taxi_auto:
            get_taxi_auto.taxi_status = False
            order_taxi = TaxiOrder(
                client_name=client_name,
                phone_number=phone_number,
                address=address,
                desired_time=desired_time,
                taxi_auto=get_taxi_auto
            )
            order_taxi.save()
            get_taxi_auto.save()
        else:
            messages.error(self.request, 'Мы приносим свои извинения. К сожалению в данный момент все наши автомобили заняты или недоступны!')
            return redirect('taxi:home')

        return redirect('taxi:order_success')


class OrderDetailView(DetailView):
    template_name = 'order_detail.html'
    context_object_name = 'taxi_orders_list'

    def get_queryset(self):
        qs = TaxiOrder.objects.all()
        return qs


class OrderSuccessView(ListView):
    template_name = 'order_success.html'
    context_object_name = 'taxi_orders_list'

    def get_queryset(self):
        qs = TaxiOrder.objects.order_by('-id')[0]
        return qs

