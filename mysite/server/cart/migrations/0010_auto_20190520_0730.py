# Generated by Django 2.2 on 2019-05-20 01:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_auto_20190518_1314'),
        ('cart', '0009_auto_20190520_0721'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usercart',
            name='product',
        ),
        migrations.AddField(
            model_name='usercart',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='shop.Product'),
        ),
    ]
