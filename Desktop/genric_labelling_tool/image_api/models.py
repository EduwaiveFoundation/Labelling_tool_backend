from django.db import models

# Create your models here.
class glt(models.Model):
    image_name=models.CharField(max_length=50000)
    url=models.CharField(max_length=500000000)
    

    def __str__(self):
        return self.image_name