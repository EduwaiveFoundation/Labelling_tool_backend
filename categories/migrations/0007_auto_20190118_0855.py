# Generated by Django 2.1.5 on 2019-01-18 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0006_auto_20190117_1059'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='category_name',
            field=models.CharField(max_length=120),
        ),
        migrations.AlterField(
            model_name='category',
            name='image_name',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='category',
            name='time_stamp',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='labelled_img',
            name='category',
            field=models.CharField(max_length=200),
        ),
    ]
