# Generated by Django 4.1 on 2022-09-28 04:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0003_task_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='finished',
            field=models.BooleanField(blank=True, null=True),
        ),
    ]
