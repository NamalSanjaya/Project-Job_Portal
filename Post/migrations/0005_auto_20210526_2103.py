# Generated by Django 3.1.7 on 2021-05-26 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Post', '0004_auto_20210526_0951'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(upload_to='Company/Post/'),
        ),
    ]
