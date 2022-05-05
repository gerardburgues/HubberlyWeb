# Generated by Django 3.1 on 2021-08-11 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0002_auto_20210811_0705'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact_name', models.CharField(max_length=200)),
                ('contact_email', models.EmailField(max_length=254)),
                ('message', models.CharField(max_length=10000)),
            ],
        ),
    ]