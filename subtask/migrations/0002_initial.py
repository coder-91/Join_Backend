# Generated by Django 5.0.4 on 2024-07-11 19:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('subtask', '0001_initial'),
        ('task', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='subtask',
            name='task',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subtasks', to='task.task'),
        ),
    ]
