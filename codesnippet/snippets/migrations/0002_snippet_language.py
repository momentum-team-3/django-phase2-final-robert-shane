# Generated by Django 3.1 on 2020-09-03 02:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='snippet',
            name='language',
            field=models.CharField(default='HTML', max_length=50),
        ),
    ]
