# Generated by Django 3.2.10 on 2021-12-31 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('language', '0003_language_nameinnativescript'),
    ]

    operations = [
        migrations.AddField(
            model_name='language',
            name='greetingInNativeScript',
            field=models.CharField(default='வணக்கம்', max_length=20),
            preserve_default=False,
        ),
    ]
