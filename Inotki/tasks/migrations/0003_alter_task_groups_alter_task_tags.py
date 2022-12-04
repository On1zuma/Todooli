# Generated by Django 4.1.3 on 2022-12-04 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0002_group_tag_task_groups_task_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='groups',
            field=models.ManyToManyField(blank=True, null=True, related_name='tasks_groups', to='tasks.group'),
        ),
        migrations.AlterField(
            model_name='task',
            name='tags',
            field=models.ManyToManyField(blank=True, null=True, related_name='tasks_tags', to='tasks.tag'),
        ),
    ]
