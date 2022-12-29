# Generated by Django 4.1.3 on 2022-12-29 18:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tasks', '0003_remove_tag_user_tag_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tag',
            name='user',
        ),
        migrations.AddField(
            model_name='tag',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
