# Generated by Django 2.2 on 2019-04-18 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onepage', '0005_auto_20190418_0758'),
    ]

    operations = [
        migrations.CreateModel(
            name='Offer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('main_title', models.CharField(max_length=255)),
                ('title', models.CharField(max_length=255)),
                ('text', models.TextField()),
                ('background_image', models.ImageField(upload_to='offer/')),
            ],
        ),
        migrations.DeleteModel(
            name='OfferSection',
        ),
    ]
