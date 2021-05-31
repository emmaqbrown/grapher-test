from django.urls import path

from . import views

urlpatterns = [
    # path('', views.GraphView.as_view(), name='graph'),
    # path('chart/', views.charts, name='charts'),
    path('', views.ChartForm.as_view(), name='home'),
    path('category-form/', views.CategoryForm.as_view(), name='category-form'),

    path('pie-chart/', views.pie_chart, name='pie-chart'),
    path('bar-chart/', views.bar_chart, name='bar-chart'),

]