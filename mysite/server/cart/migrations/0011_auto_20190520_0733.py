# Generated by Django 2.2 on 2019-05-20 01:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_auto_20190518_1314'),
        ('cart', '0010_auto_20190520_0730'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usercart',
            name='product',
        ),
        migrations.AddField(
            model_name='usercart',
            name='product',
            field=models.ManyToManyField(null=True, to='shop.Product'),
        ),
    ]
