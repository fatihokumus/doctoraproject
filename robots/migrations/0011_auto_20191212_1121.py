# Generated by Django 2.2.5 on 2019-12-12 08:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('robots', '0010_auto_20191212_1120'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='taskhistory',
            name='TransferredObject',
        ),
        migrations.RemoveField(
            model_name='tobjectwaiting',
            name='TransferredObject',
        ),
    ]