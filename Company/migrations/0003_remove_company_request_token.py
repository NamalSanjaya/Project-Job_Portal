# Generated by Django 3.1.7 on 2021-05-21 12:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Company', '0002_company_request_token'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='company_request',
            name='token',
        ),
    ]
