# Generated by Django 3.1.7 on 2021-05-21 05:02

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company_Request',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('registered_name', models.CharField(max_length=30)),
                ('registered_no', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('contact_no', models.CharField(max_length=20)),
                ('date_requested', models.DateTimeField(default=django.utils.timezone.now)),
                ('doc_Buisness', models.FileField(upload_to='Company/Company_Request/%d/')),
            ],
        ),
    ]
