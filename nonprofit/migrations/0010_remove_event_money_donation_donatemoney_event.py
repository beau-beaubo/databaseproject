# Generated by Django 5.1 on 2024-11-28 15:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nonprofit', '0009_remove_donatestuff_category_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='money_donation',
        ),
        migrations.AddField(
            model_name='donatemoney',
            name='event',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='nonprofit.event'),
        ),
    ]