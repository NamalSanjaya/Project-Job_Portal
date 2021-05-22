# Generated by Django 3.1.7 on 2021-05-21 19:02

import Seeker.models
from django.db import migrations, models
import django.utils.timezone
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('Seeker', '0011_auto_20210521_1853'),
    ]

    operations = [
        migrations.CreateModel(
            name='Seeker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('contact_no', models.CharField(max_length=20)),
                ('date_saved', models.DateTimeField(default=django.utils.timezone.now)),
                ('doc_Local_Police', models.FileField(upload_to='Seeker/Seeker_Request/%d/LP/')),
                ('doc_Gramma_Niladari', models.FileField(upload_to='Seeker/Seeker_Request/%d/GN')),
                ('doc_Divisional_Secretary', models.FileField(upload_to='Seeker/Seeker_Request/%d/DS')),
                ('token', models.CharField(default=Seeker.models.secret_token, max_length=16)),
                ('skills', multiselectfield.db.fields.MultiSelectField(choices=[('Design', (('Logo_Designer', 'Logo Designer'), ('Web_Designer', 'Web Designer'), ('Print_Designer', 'Print Designer'))), ('Technology', (('Mobile_App_Developer', 'Mobile App Developer'), ('Software_Engineer', 'Software Enginner'), ('DataBase_Engineer', 'DataBase Engineer'), ('System_Engineer', 'System Engineer'))), ('Entertainment', (('Content_Writer', 'Content Writer'), ('Video_Editer', 'Video Editer')))], max_length=200)),
            ],
        ),
    ]
