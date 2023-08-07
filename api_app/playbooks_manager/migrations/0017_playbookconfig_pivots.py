# Generated by Django 4.1.9 on 2023-06-14 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("pivots_manager", "0001_initial"),
        ("playbooks_manager", "0016_playbookconfig_disabled_in_organizations"),
    ]

    operations = [
        migrations.AddField(
            model_name="playbookconfig",
            name="pivots",
            field=models.ManyToManyField(
                blank=True,
                related_name="used_by_playbooks",
                to="pivots_manager.pivotconfig",
            ),
        ),
    ]