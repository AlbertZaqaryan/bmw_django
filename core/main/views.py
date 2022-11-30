from django.shortcuts import render
from .models import Car
from django.views.generic import ListView
# Create your views here.

class HomeListView(ListView):
    template_name = 'home.html'

    def get(self, request):
        cars = Car.objects.all()
        return render(request, self.template_name, {'cars':cars})
