# Generated by Django 4.2.7 on 2023-11-28 11:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_remove_blog_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='LabelCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Label Name')),
            ],
        ),
        migrations.AddField(
            model_name='blog',
            name='category',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='app.categoryblog', verbose_name='Category'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='blog',
            name='label',
            field=models.ManyToManyField(to='app.labelcategory', verbose_name="Label's"),
        ),
    ]