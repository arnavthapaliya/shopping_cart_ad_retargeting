# Generated by Django 2.2 on 2019-05-19 13:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_auto_20190518_1314'),
        ('cart', '0006_auto_20190519_0911'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usercart',
            old_name='created_at',
            new_name='timestamp',
        ),
        migrations.RenameField(
            model_name='usercart',
            old_name='updated_at',
            new_name='updated',
        ),
        migrations.RemoveField(
            model_name='usercart',
            name='active',
        ),
        migrations.RemoveField(
            model_name='usercart',
            name='product',
        ),
        migrations.RemoveField(
            model_name='usercart',
            name='quantity',
        ),
        migrations.AddField(
            model_name='usercart',
            name='products',
            field=models.ManyToManyField(blank=True, to='shop.Product'),
        ),
        migrations.AddField(
            model_name='usercart',
            name='total',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=100),
        ),
        migrations.AlterField(
            model_name='usercart',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
