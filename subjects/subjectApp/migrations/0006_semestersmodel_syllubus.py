# Generated by Django 4.1.2 on 2022-10-08 05:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subjectApp', '0005_alter_semestersmodel_semester'),
    ]

    operations = [
        migrations.AddField(
            model_name='semestersmodel',
            name='syllubus',
            field=models.FileField(default=type(None), upload_to='uploads/'),
        ),
    ]
