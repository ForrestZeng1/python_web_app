# Generated by Django 2.2 on 2019-04-22 01:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstApp', '0004_auto_20190422_0124'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='gender',
            field=models.CharField(choices=[('male', 'Male'), ('female', 'Female')], max_length=6),
        ),
    ]
