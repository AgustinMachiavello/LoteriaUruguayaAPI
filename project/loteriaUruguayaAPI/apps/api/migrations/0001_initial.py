# Generated by Django 2.2.5 on 2019-09-25 13:27

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('game_id', models.AutoField(primary_key=True, serialize=False)),
                ('game_name', models.CharField(max_length=50, unique=True)),
                ('game_update_date', models.PositiveIntegerField(choices=[(1, 'Monday'), (2, 'Tuesday'), (3, 'Wednesday'), (4, 'Thursday'), (5, 'Friday'), (6, 'Saturday'), (7, 'Sunday')])),
                ('game_update_time', models.TimeField()),
                ('game_created_at', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('game_updated_at', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('game_has_unique_result_per_day', models.BooleanField()),
            ],
            options={
                'ordering': ['-game_id', '-game_created_at'],
            },
        ),
        migrations.CreateModel(
            name='Result',
            fields=[
                ('result_id', models.AutoField(primary_key=True, serialize=False)),
                ('result_date', models.DateField(default=django.utils.timezone.now)),
                ('result_created_at', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('result_updated_at', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('result_game_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='results', to='api.Game')),
            ],
        ),
        migrations.CreateModel(
            name='VespertineNocturneResult',
            fields=[
                ('result_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='api.Result')),
                ('vn_result_is_vespertine', models.BooleanField()),
            ],
            bases=('api.result',),
        ),
    ]