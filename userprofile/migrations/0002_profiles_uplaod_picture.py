# Generated by Django 4.0 on 2023-05-06 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profiles',
            name='uplaod_picture',
            field=models.ImageField(default=2, upload_to='profile'),
        ),
    ]
