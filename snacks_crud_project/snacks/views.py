from django.shortcuts import render
from django.views.generic import (
                                    ListView,
                                    CreateView,
                                    UpdateView,
                                    DeleteView,
                                    DetailView
                                )
from .models import Snack 

# Create your views here.

class SnackListView(ListView):
    template_name= 'snacks_list.html'
    model =Snack


class SnackCreateView(CreateView):
    template_name= 'snack_create.html'
    model =Snack

class SnackUpdateView(UpdateView):
    template_name= 'snack_update.html'
    model =Snack

class SnackDeleteView(DeleteView):
    template_name= 'snack_delete.html'
    model =Snack

