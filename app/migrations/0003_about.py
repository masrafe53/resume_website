# Generated by Django 4.1.2 on 2022-10-12 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_work'),
    ]

    operations = [
        migrations.CreateModel(
            name='about',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img1', models.ImageField(upload_to='media')),
                ('title1', models.CharField(max_length=60)),
                ('dis1', models.TextField(max_length=500)),
                ('img2', models.ImageField(upload_to='media')),
                ('title2', models.CharField(max_length=60)),
                ('dis2', models.TextField(max_length=500)),
            ],
        ),
    ]
