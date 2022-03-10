# Generated by Django 3.2.12 on 2022-03-09 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('description', models.CharField(max_length=250)),
                ('image', models.ImageField(upload_to='portfolio/images')),
                ('url', models.URLField(blank=True)),
            ],
        ),
    ]