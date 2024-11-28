# Generated by Django 5.1 on 2024-11-28 08:23

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nonprofit', '0006_alter_donatemoney_date_alter_donatestuff_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='money_donation',
            field=models.ForeignKey(blank=True, default=django.utils.timezone.now, null=True, on_delete=django.db.models.deletion.CASCADE, to='nonprofit.donatemoney'),
        ),
        migrations.AlterField(
            model_name='event',
            name='stuff_donation',
            field=models.ForeignKey(blank=True, default=django.utils.timezone.now, null=True, on_delete=django.db.models.deletion.CASCADE, to='nonprofit.donatestuff'),
        ),
    ]
