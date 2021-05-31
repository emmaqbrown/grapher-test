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
    success_url = '/bar-chart'


    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.

        form.save()
        return super().form_valid(form)

class CategoryForm(FormView):
    template_name = 'grapher/category-form.html'
    form_class = CategoryForm
    success_url = '/bar-chart'


    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.

        form.save()
        return super().form_valid(form)

def choose_colors(num):
    ''' Returns list of colors with `num` length. 
        Picks a single color then finds different opacity levels
        of that color. 
    '''
    colors = []

    red = randint(0, 256)
    green = randint(0, 256)
    blue = randint(0, 256)

    for i in range(num):
        a = uniform(0, 1)
        
        colors.append('rgba({}, {}, {},{})'.format(red,green,blue,a))

    return colors
 
def pie_chart(request):
    labels = []
    data = []
 
    chart = Chart.objects.all()[0]
    for category in chart.category_set.all():
        labels.append(category.label)
        data.append(category.value)
 
    return render(request, 'grapher/piechart2.html', {
        'labels': labels,
        'data': data,
        'title': [chart.title],
        'colors': choose_colors(len(labels))
    })

def bar_chart(request):
    labels = []
    data = []
 
    chart = Chart.objects.all()[1]
    for category in chart.category_set.all():
        labels.append(category.label)
        data.append(category.value)
 
    return render(request, 'grapher/barchart.html', {
        'labels': labels,
        'data': data,
        'title': [chart.title],
        'colors': choose_colors(len(labels))
    })

    

