# Generated by Django 4.1.5 on 2023-02-02 13:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_alter_task_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='User',
            new_name='user',
        ),
    ]
