# Generated by Django 2.2 on 2019-04-24 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onepage', '0017_remove_project_text'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='callsection',
            name='text',
        ),
        migrations.RemoveField(
            model_name='callsection',
            name='title',
        ),
        migrations.AddField(
            model_name='callsection',
            name='button_text',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]