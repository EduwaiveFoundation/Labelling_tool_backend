from django.db import models

# Create your models here.
class category(models.Model):
    image_name=models.CharField(max_length=50)
    category_name=models.CharField(max_length=20)
    time_stamp=models.CharField(max_length=50)

    def __str__(self):
        return self.category_name

class labelled_img(models.Model):
    image_name=models.CharField(max_length=300)
    category=models.CharField(max_length=20)
    
    def __str__(self):
        return self.image_path

