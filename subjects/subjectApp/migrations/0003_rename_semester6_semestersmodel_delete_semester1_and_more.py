# Generated by Django 4.1.2 on 2022-10-07 16:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('subjectApp', '0002_semester2_semester3_semester4_semester5_semester6_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='semester6',
            new_name='semestersModel',
        ),
        migrations.DeleteModel(
            name='semester1',
        ),
        migrations.DeleteModel(
            name='semester2',
        ),
        migrations.DeleteModel(
            name='semester3',
        ),
        migrations.DeleteModel(
            name='semester4',
        ),
        migrations.DeleteModel(
            name='semester5',
        ),
        migrations.DeleteModel(
            name='semester7',
        ),
        migrations.DeleteModel(
            name='semester8',
        ),
    ]
