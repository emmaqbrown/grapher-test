from django.urls import path

from . import views

urlpatterns = [
    path('', views.AllCharts.as_view(), name='all-charts'),
    path('chart-form', views.ChartForm.as_view(), name='chart-form'),
    path('category-form/', views.CategoryForm.as_view(), name='category-form'),

    path('pie-chart/<str:pk>/', views.pie_chart, name='pie-chart'),
    path('bar-chart/<str:pk>/', views.bar_chart, name='bar-chart'),

]