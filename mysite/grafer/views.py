from typing import List
from django.forms.models import modelformset_factory, modelform_factory
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import FormView
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login, authenticate
from django.db.models import Q
from django.shortcuts import render
from .forms import *

from .models import *
from random import randint, uniform


class ChartForm(FormView):
    template_name = 'grapher/chart-form.html'
    form_class = ChartForm
    success_url = '/'


    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.

        form.save()
        return super().form_valid(form)

class CategoryForm(FormView):
    template_name = 'grapher/category-form.html'
    form_class = CategoryForm
    success_url = '/'


    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.

        form.save()
        return super().form_valid(form)

def category_form_test(request):
    # if this is a POST request we need to process the form data
    CategoryFormSet = modelform_factory(Category, fields=('label','value','chart'))
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = CategoryFormSet(request.POST)
        form.save()
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            chart_title = form.chart
            return HttpResponseRedirect('grapher/bar-chart',chart_title=chart_title)

    # if a GET (or any other method) we'll create a blank form
    else:
        form = CategoryFormSet()

    return render(request, 'grapher/category-form.html', {'form': form})

def choose_colors(num):
    ''' Returns list of colors with `num` length. 
        Picks a single color then finds different opacity levels
        of that color. 
    '''
    colors = []
    
    
    red = randint(0, 255)
    green = randint(0, 255)
    blue = randint(0, 255)

    for i in range(num):
        red += 25
        green += 25
        blue += 50

        
        colors.append('rgb({}, {}, {})'.format(red,green,blue))

    return colors
 
def pie_chart(request,pk):
    labels = []
    data = []
 
    chart = Chart.objects.filter(title=pk)[0]
    for category in chart.category_set.all():
        labels.append(category.label)
        data.append(category.value)
 
    return render(request, 'grapher/piechart2.html', {
        'labels': labels,
        'data': data,
        'title': [chart.title],
        'colors': choose_colors(len(labels))
    })

def bar_chart(request,pk):
    labels = []
    data = []

    chart = Chart.objects.filter(title=pk)[0]
    for category in chart.category_set.all():
        labels.append(category.label)
        data.append(category.value)
 
    return render(request, 'grapher/barchart.html', {
        'labels': labels,
        'data': data,
        'title': [chart.title],
        'colors': choose_colors(len(labels))
    })


class AllCharts(ListView):
    template_name = 'grapher/all-charts.html'
    model = Chart

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['charts'] = self.model.objects.all()
        return context

