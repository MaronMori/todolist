# Generated by Django 4.1 on 2023-10-04 20:59

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("ToDoListApp", "0002_rename_task_todolist_tasks"),
    ]

    operations = [
        migrations.RenameField(
            model_name="todolist",
            old_name="tasks",
            new_name="task",
        ),
    ]