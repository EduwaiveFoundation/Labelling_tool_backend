from django.contrib import admin
from .models import category
from .models import labelled_img
# Register your models here.
admin.site.register(category);
admin.site.register(labelled_img)