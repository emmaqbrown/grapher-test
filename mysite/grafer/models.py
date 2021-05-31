from django.db import models

# Create your models here.




class Chart(models.Model):
    title = models.TextField()

    def __str__(self):
        return self.title
        
class Category(models.Model):
    label = models.TextField()
    value = models.PositiveIntegerField()
    chart = models.ForeignKey(Chart, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.label


