# Generated by Django 4.2 on 2023-06-01 05:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libraryapp', '0004_lr_addbook'),
    ]

    operations = [
        migrations.AddField(
            model_name='lr_addbook',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='li_bookadd'),
        ),
    ]