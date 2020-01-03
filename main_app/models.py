from django.db import models


#Company model, the one side on our relation 
class Wish(models.Model):
    description = models.CharField(max_length=100)
    quantity = models.IntegerField(default=1)
    def __str__(self):
        return self.description
        