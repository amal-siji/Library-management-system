# Generated by Django 4.2 on 2023-06-02 04:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libraryapp', '0008_lr_addbook_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lr_addbook',
            name='image',
            field=models.ImageField(null=True, upload_to='li_bookadd'),
        ),
    ]
