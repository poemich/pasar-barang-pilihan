# Generated by Django 5.1.1 on 2024-09-08 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('price', models.FloatField()),
                ('description', models.TextField()),
            ],
        ),
    ]
