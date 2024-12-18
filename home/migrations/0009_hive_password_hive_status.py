# Generated by Django 5.1.3 on 2024-11-29 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_message_audio'),
    ]

    operations = [
        migrations.AddField(
            model_name='hive',
            name='password',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='hive',
            name='status',
            field=models.CharField(choices=[('public', 'Public'), ('private', 'Private')], default='public', max_length=10),
        ),
    ]
