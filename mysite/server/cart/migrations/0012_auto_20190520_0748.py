# Generated by Django 2.2 on 2019-05-20 02:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0011_auto_20190520_0733'),
    ]

    operations = [
        migrations.CreateModel(
            name='account_data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=30)),
                ('key', models.CharField(max_length=30)),
                ('value', models.CharField(blank=True, max_length=30, null=True)),
            ],
            options={
                'unique_together': {('username', 'key')},
            },
        ),
        migrations.DeleteModel(
            name='UserCart',
        ),
    ]
