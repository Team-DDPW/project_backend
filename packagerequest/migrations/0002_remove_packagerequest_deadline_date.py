# Generated by Django 3.2.9 on 2021-11-11 02:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('packagerequest', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='packagerequest',
            name='deadline_date',
        ),
    ]