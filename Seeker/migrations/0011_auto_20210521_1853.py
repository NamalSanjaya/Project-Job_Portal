# Generated by Django 3.1.7 on 2021-05-21 13:23

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('Seeker', '0010_seeker_request_token'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seeker_request',
            name='skills',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('Design', (('Logo_Designer', 'Logo Designer'), ('Web_Designer', 'Web Designer'), ('Print_Designer', 'Print Designer'))), ('Technology', (('Mobile_App_Developer', 'Mobile App Developer'), ('Software_Engineer', 'Software Enginner'), ('DataBase_Engineer', 'DataBase Engineer'), ('System_Engineer', 'System Engineer'))), ('Entertainment', (('Content_Writer', 'Content Writer'), ('Video_Editer', 'Video Editer')))], max_length=200),
        ),
    ]
