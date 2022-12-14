# Generated by Django 4.0.6 on 2022-08-06 03:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AnimalClass',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('classification', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Continents',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('continent', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Countries',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(max_length=100)),
                ('continent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='totemApp.continents')),
            ],
        ),
        migrations.CreateModel(
            name='Vertebrates',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('animal', models.CharField(max_length=70)),
                ('meaning', models.TextField(max_length=1000)),
                ('classification', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='totemApp.animalclass')),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='totemApp.countries')),
            ],
        ),
        migrations.CreateModel(
            name='Invertebrates',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('animal', models.CharField(max_length=70)),
                ('meaning', models.TextField(max_length=1000)),
                ('classification', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='totemApp.animalclass')),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='totemApp.countries')),
            ],
        ),
    ]
