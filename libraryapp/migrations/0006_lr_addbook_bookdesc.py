# Generated by Django 4.2 on 2023-06-01 05:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libraryapp', '0005_lr_addbook_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='lr_addbook',
            name='bookdesc',
            field=models.TextField(null=True),
        ),
    ]
