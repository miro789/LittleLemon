# Generated by Django 5.1.2 on 2024-10-24 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0003_menuitem_image_url'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='menuitem',
            name='image_url',
        ),
        migrations.AddField(
            model_name='menuitem',
            name='image_name',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
