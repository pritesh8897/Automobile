# Generated by Django 3.0.7 on 2020-06-16 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Verna', '0002_final_selected_car_owner_selected_car_colour'),
    ]

    operations = [
        migrations.AlterField(
            model_name='owner',
            name='car_name',
            field=models.ManyToManyField(blank=True, null=True, to='Verna.final_selected_car'),
        ),
    ]
