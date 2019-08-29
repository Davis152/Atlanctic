from django.shortcuts import render
from .models import Record
from django.views.generic import ListView, DetailView, CreateView

def home(request):

    context = {
        'records': Record.objects.all()
    }

    return render(request, 'record/home.html',context)

class RecordListView(ListView):
        model = Record
        template_name = 'record/home.html'
        context_object_name = 'records'
        ordering =     ['-date_posted' ]

class RecordDetailView(DetailView):
        model = Record


class RecordCreateView(CreateView):
    model = Record
    fields = ['country','program']


def about(request):
    return render(request, 'record/about.html',  {'title':'About'})
