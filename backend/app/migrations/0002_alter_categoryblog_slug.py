# Generated by Django 4.2.7 on 2023-11-28 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categoryblog',
            name='slug',
            field=models.SlugField(blank=True, editable=False, verbose_name='Slug'),
        ),
    ]