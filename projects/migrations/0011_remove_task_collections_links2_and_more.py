# Generated by Django 4.0 on 2023-05-15 18:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0010_alter_task_task_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task_collections',
            name='links2',
        ),
        migrations.RemoveField(
            model_name='task_collections',
            name='links3',
        ),
    ]
