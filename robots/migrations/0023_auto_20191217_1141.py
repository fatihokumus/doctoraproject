# Generated by Django 2.2.4 on 2019-12-17 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('robots', '0022_auto_20191217_1138'),
    ]

    operations = [
        migrations.AlterField(
            model_name='robotlocation',
            name='LocationTime',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='robottaskhistorylog',
            name='LogTime',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='transferredobject',
            name='CreatedOn',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
