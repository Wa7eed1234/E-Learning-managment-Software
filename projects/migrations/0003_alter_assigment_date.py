# Generated by Django 4.0 on 2023-05-13 00:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_assigment_score'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assigment',
            name='date',
            field=models.DateField(auto_now_add=True),
        ),
    ]
