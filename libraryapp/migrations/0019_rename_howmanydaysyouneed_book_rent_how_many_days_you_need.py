# Generated by Django 4.2 on 2023-06-07 05:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('libraryapp', '0018_li_message'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book_rent',
            old_name='HowMAnyDaysYouNeed',
            new_name='How_many_days_you_need',
        ),
    ]
