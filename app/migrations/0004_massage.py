# Generated by Django 4.1.2 on 2022-10-12 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_about'),
    ]

    operations = [
        migrations.CreateModel(
            name='massage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('sub', models.CharField(max_length=100)),
                ('text', models.TextField(max_length=500)),
            ],
        ),
    ]