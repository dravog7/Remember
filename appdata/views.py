from django.shortcuts import render
from django.views.generic import ListView,CreateView
from .models import data
# Create your views here.

class dataListView(ListView):
    model=data
    paginate_by=100

    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        return context

class dataView(CreateView):
    model=data
    fields=['info']
    url='..'
