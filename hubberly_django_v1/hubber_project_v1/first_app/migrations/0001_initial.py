# Generated by Django 3.1 on 2021-08-10 14:19

from django.db import migrations, models
import django.forms.widgets


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactForm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact_name', models.CharField(max_length=200)),
                ('contact_email', models.EmailField(max_length=254)),
                ('message', models.CharField(max_length=10000)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=264)),
                ('user_email', models.EmailField(max_length=254)),
                ('user_password', models.CharField(max_length=10, verbose_name=django.forms.widgets.PasswordInput)),
            ],
        ),
    ]