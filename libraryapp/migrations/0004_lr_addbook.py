# Generated by Django 4.2 on 2023-06-01 05:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libraryapp', '0003_remove_cu_profile_gender_remove_cu_profile_phoneno_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='lr_addbook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bookname', models.CharField(max_length=255)),
                ('author', models.CharField(max_length=255)),
                ('date', models.DateField(null=True)),
            ],
        ),
    ]