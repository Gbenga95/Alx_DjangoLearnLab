# Generated by Django 5.2.4 on 2025-07-14 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookshelf', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='publication_year',
            field=models.IntegerField(default=2000),
        ),
    ]
