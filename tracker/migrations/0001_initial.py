# Generated by Django 5.2.1 on 2025-05-21 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MoodEntry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True)),
                ('mood', models.CharField(max_length=20)),
                ('note', models.TextField(blank=True)),
            ],
        ),
    ]
