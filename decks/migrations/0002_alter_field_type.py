# Generated by Django 4.1.2 on 2022-10-10 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('decks', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='field',
            name='type',
            field=models.CharField(choices=[('main', 'main'), ('secondary', 'secondary')], max_length=9),
        ),
    ]
