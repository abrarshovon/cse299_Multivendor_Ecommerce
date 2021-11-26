from django.shortcuts import render, redirect

from .forms import CustomerSignUpForm, VendorSignUpForm
from .models import Customer, Vendor, CustomUser

from django.urls import reverse_lazy
from django.views import generic


class SignUpView(generic.TemplateView):
    template_name = 'registration/signup.html'


class CustomerSignUpView(generic.CreateView):
    model = CustomUser
    form_class = CustomerSignUpForm
    template_name = 'registration/customer_signup.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'Customer'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')

class VendorSignUpView(generic.CreateView):
    model = CustomUser
    form_class = VendorSignUpForm
    template_name = 'registration/vendor_signup.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'Vendor'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')
