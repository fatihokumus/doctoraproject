# Generated by Django 2.1.3 on 2019-10-03 14:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('robots', '0015_auto_20190905_1436'),
    ]

    operations = [
        migrations.CreateModel(
            name='EndStation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Code', models.CharField(max_length=250)),
                ('Name', models.CharField(max_length=500)),
                ('isActive', models.BooleanField(default=False)),
                ('isFull', models.BooleanField(default=False)),
                ('Position', models.CharField(blank=True, max_length=2000)),
                ('CenterX', models.IntegerField(default=0)),
                ('CenterY', models.IntegerField(default=0)),
                ('Map', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='robots.Map')),
            ],
        ),

        migrations.AddField(
            model_name='taskhistory',
            name='EndStation',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='EndStation_TOTask', to='robots.EndStation'),
        ),

    ]
