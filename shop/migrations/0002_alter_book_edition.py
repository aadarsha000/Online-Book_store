# Generated by Django 4.1.3 on 2022-11-25 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='edition',
            field=models.IntegerField(),
        ),
    ]