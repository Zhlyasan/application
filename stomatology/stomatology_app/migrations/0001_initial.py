# Generated by Django 4.2.7 on 2023-11-27 18:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('surname', models.TextField(blank=True)),
                ('birth_date', models.DateTimeField(blank=True)),
                ('snils', models.CharField(max_length=14)),
                ('inn', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('surname', models.TextField(blank=True)),
                ('birth_date', models.DateTimeField(blank=True)),
                ('allergies', models.CharField(max_length=100)),
                ('sale', models.IntegerField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Session',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_time', models.DateTimeField(blank=True)),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stomatology_app.doctor')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stomatology_app.patient')),
            ],
        ),
        migrations.CreateModel(
            name='Worklist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(blank=True, null=True)),
                ('cost', models.FloatField(blank=True)),
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stomatology_app.session')),
            ],
        ),
    ]