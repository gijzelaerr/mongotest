from django.views.generic.edit import CreateView
from .models import Something


class SomethingCreate(CreateView):
    model = Something
    success_url = '/create/'
    fields = ('some_field',)