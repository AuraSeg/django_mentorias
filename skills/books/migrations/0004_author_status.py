# Generated by Django 4.0.3 on 2022-04-05 03:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_book_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='status',
            field=models.BooleanField(default=True, verbose_name='Status'),
        ),
    ]