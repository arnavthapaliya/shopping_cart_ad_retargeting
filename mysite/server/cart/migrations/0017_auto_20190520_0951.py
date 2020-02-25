# Generated by Django 2.2 on 2019-05-20 04:06

from django.db import migrations, models
import shop.models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_auto_20190518_1314'),
        ('cart', '0016_auto_20190520_0949'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usercart',
            name='product',
        ),
        migrations.AddField(
            model_name='usercart',
            name='product',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name=shop.models.Product),
        ),
        migrations.RemoveField(
            model_name='usercart',
            name='quantity',
        ),
        migrations.AddField(
            model_name='usercart',
            name='quantity',
            field=models.ManyToManyField(default=1, to='shop.Product'),
        ),
    ]