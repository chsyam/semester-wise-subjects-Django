# Generated by Django 4.1.2 on 2022-10-08 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subjectApp', '0006_semestersmodel_syllubus'),
    ]

    operations = [
        migrations.AlterField(
            model_name='semestersmodel',
            name='syllubus',
            field=models.FileField(null=True, upload_to=''),
        ),
    ]
