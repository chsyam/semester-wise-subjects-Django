# Generated by Django 4.1.2 on 2022-10-08 04:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subjectApp', '0003_rename_semester6_semestersmodel_delete_semester1_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='semestersmodel',
            name='semester',
            field=models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3')], default=1),
        ),
    ]
