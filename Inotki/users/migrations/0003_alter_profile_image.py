# Generated by Django 4.1.3 on 2022-12-28 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(blank='/profile_pics/default.jpg', default='/profile_pics/default.jpg', null='/profile_pics/default.jpg', upload_to='profile_pics'),
        ),
    ]