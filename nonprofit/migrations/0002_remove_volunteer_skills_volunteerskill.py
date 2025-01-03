# Generated by Django 5.1.3 on 2024-11-17 12:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nonprofit', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='volunteer',
            name='skills',
        ),
        migrations.CreateModel(
            name='VolunteerSkill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skill', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nonprofit.skill')),
                ('volunteer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nonprofit.volunteer')),
            ],
        ),
    ]
