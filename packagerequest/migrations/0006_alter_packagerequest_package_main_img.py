# Generated by Django 3.2.9 on 2021-11-11 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('packagerequest', '0005_alter_packagerequest_package_main_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='packagerequest',
            name='package_Main_Img',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
