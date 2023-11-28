# Generated by Django 4.2.7 on 2023-11-28 11:07

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_alter_categoryblog_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categoryblog',
            name='slug',
            field=autoslug.fields.AutoSlugField(always_update=True, blank=True, editable=False, populate_from='name'),
        ),
    ]
