# Generated by Django 3.0.7 on 2020-07-22 06:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Verna', '0006_ownerinformation_phone_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ownerinformation',
            name='phone_number',
        ),
        migrations.AddField(
            model_name='carinformation',
            name='color',
            field=models.CharField(default='white', max_length=10),
        ),
    ]
