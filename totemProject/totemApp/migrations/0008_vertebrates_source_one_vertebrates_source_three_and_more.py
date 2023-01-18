# Generated by Django 4.0.6 on 2023-01-16 02:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('totemApp', '0007_remove_vertebrates_sources'),
    ]

    operations = [
        migrations.AddField(
            model_name='vertebrates',
            name='source_one',
            field=models.TextField(default='URL', max_length=1000),
        ),
        migrations.AddField(
            model_name='vertebrates',
            name='source_three',
            field=models.TextField(blank=True, max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='vertebrates',
            name='source_two',
            field=models.TextField(blank=True, max_length=1000, null=True),
        ),
    ]