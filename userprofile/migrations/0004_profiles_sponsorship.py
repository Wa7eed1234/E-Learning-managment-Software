# Generated by Django 4.0 on 2023-06-07 05:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0003_remove_profiles_social_profiles_facebook_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='profiles',
            name='sponsorship',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
