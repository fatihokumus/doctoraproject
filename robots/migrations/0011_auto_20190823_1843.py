# Generated by Django 2.1.3 on 2019-08-23 15:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('robots', '0010_auto_20181126_1437'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChargingStation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Code', models.CharField(max_length=250)),
                ('Name', models.CharField(max_length=500)),
                ('isActive', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='ChargingStationSection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Code', models.CharField(max_length=250)),
                ('Name', models.CharField(max_length=500)),
                ('isActive', models.BooleanField(default=False)),
                ('isFull', models.BooleanField(default=False)),
                ('Position', models.CharField(blank=True, max_length=2000)),
                ('ChargingStation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='robots.ChargingStation')),
            ],
        ),
        migrations.CreateModel(
            name='MapGoalPoint',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Code', models.CharField(max_length=50)),
                ('Left', models.IntegerField()),
                ('Right', models.IntegerField()),
                ('Top', models.IntegerField()),
                ('Bottom', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='ObstaclePoint',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Left', models.IntegerField()),
                ('Right', models.IntegerField()),
                ('Top', models.IntegerField()),
                ('Bottom', models.IntegerField()),
                ('CenterX', models.IntegerField()),
                ('CenterY', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='TaskHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('WorkOrder', models.IntegerField(null=True)),
                ('isCompleted', models.BooleanField(default=False)),
                ('isActive', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='TransferredObjects',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Borcode', models.CharField(max_length=250)),
                ('isActive', models.BooleanField(default=False)),
                ('LastPosX', models.IntegerField(null=True)),
                ('LastPosY', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='TransferredObjectsTask',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Code', models.CharField(max_length=250)),
                ('isCompleted', models.BooleanField(default=False)),
                ('isActive', models.BooleanField(default=False)),
                ('TransferredObjects', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='robots.TransferredObjects')),
            ],
        ),
        migrations.CreateModel(
            name='WaitingStation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Code', models.CharField(max_length=250)),
                ('Name', models.CharField(max_length=500)),
                ('isActive', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='WaitingStationSection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Code', models.CharField(max_length=250)),
                ('Name', models.CharField(max_length=500)),
                ('isActive', models.BooleanField(default=False)),
                ('isFull', models.BooleanField(default=False)),
                ('Position', models.CharField(blank=True, max_length=2000)),
            ],
        ),
        migrations.CreateModel(
            name='WorkStation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Code', models.CharField(max_length=250)),
                ('Name', models.CharField(max_length=500)),
                ('isActive', models.BooleanField(default=False)),
                ('Position', models.CharField(blank=True, max_length=2000)),
                ('EnterPosX', models.FloatField()),
                ('EnterPosY', models.FloatField()),
                ('ExitPosX', models.FloatField()),
                ('ExitPosY', models.FloatField()),
            ],
        ),
        migrations.RemoveField(
            model_name='robot',
            name='SubNet',
        ),
        migrations.RemoveField(
            model_name='robot',
            name='Tenant',
        ),
        migrations.AddField(
            model_name='map',
            name='Distance',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='map',
            name='Height',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='map',
            name='Width',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='robot',
            name='LastCoordX',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='robot',
            name='LastCoordY',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='robot',
            name='Map',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='robots.Map'),
        ),
        migrations.AddField(
            model_name='robot',
            name='isActive',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='workstation',
            name='Map',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='robots.Map'),
        ),
        migrations.AddField(
            model_name='waitingstationsection',
            name='Map',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='robots.Map'),
        ),
        migrations.AddField(
            model_name='waitingstationsection',
            name='TransferredObjects',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='robots.TransferredObjects'),
        ),
        migrations.AddField(
            model_name='waitingstationsection',
            name='WaitingStation',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='robots.WaitingStation'),
        ),
        migrations.AddField(
            model_name='waitingstation',
            name='Map',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='robots.Map'),
        ),
        migrations.AddField(
            model_name='transferredobjects',
            name='Map',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='robots.Map'),
        ),
        migrations.AddField(
            model_name='taskhistory',
            name='Robot',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='Robot_TOTask', to='robots.Robot'),
        ),
        migrations.AddField(
            model_name='taskhistory',
            name='TransferredObjectsTask',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='robots.TransferredObjectsTask'),
        ),
        migrations.AddField(
            model_name='taskhistory',
            name='WorkStation',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='WorkStation_TOTask', to='robots.WorkStation'),
        ),
        migrations.AddField(
            model_name='obstaclepoint',
            name='Map',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='robots.Map'),
        ),
        migrations.AddField(
            model_name='mapgoalpoint',
            name='Map',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='robots.Map'),
        ),
        migrations.AddField(
            model_name='chargingstationsection',
            name='Robot',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='robots.Robot'),
        ),
        migrations.AddField(
            model_name='chargingstation',
            name='Map',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='robots.Map'),
        ),
    ]
