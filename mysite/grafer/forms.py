from django import forms 
from .models import Chart, Category 




# create a ModelForm 
class ChartForm(forms.ModelForm): 
    class Meta: 
        model = Chart 
        fields = (
            'title',
            )

class CategoryForm(forms.ModelForm): 
    class Meta: 
        model = Category 
        fields = (
            'label',
            'value',
            'chart'
            )


