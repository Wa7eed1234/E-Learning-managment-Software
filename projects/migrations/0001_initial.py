# Generated by Django 4.0 on 2023-05-06 09:28

import ckeditor_uploader.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('dash', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField(auto_created=True)),
                ('ending_date', models.DateTimeField(auto_created=True)),
                ('project_name', models.CharField(max_length=200)),
                ('status', models.CharField(choices=[('expired', 'expired'), ('active', 'active')], max_length=200)),
                ('descriptions', ckeditor_uploader.fields.RichTextUploadingField(blank=True)),
                ('cohorts', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dash.cohorts')),
            ],
        ),
    ]
