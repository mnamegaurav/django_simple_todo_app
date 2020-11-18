from django.db import models

# Create your models here.


class ToDo(models.Model):
    text = models.CharField(max_length=50)
    added_on = models.DateTimeField(auto_now_add = True)
    updated_on = models.DateTimeField(auto_now = True)

    def __str__(self): 
        return self.text

    class Meta:
        ordering = ['-updated_on']