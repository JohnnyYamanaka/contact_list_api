# Generated by Django 3.0.2 on 2020-01-08 01:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contactlist', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='telegramAccount',
            field=models.CharField(blank=True, max_length=45, null=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='twitterAccount',
            field=models.CharField(blank=True, max_length=45, null=True),
        ),
    ]
