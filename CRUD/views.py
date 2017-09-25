# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import Persona
from django.views import generic
from django.views.generic.edit import DeleteView
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.core.urlresolvers import reverse_lazy

# Create your views here.
class IndexView(generic.ListView):
    template_name = 'CRUD/index.html'
    context_object_name = 'latest_persona_list'

    def get_queryset(self):
        return Persona.objects.order_by('name')

class CreatePersona(CreateView):
    model = Persona
    success_url = reverse_lazy('CRUD:index')
    fields = ['name', 'address', 'email']

class DeletePersona(DeleteView):
    model = Persona
    success_url = reverse_lazy('CRUD:index')

class UpdatePersona(UpdateView):
    model = Persona
    success_url = reverse_lazy('CRUD:index')
    fields = ['name', 'address', 'email']