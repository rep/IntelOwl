# Generated by Django 4.1.9 on 2023-06-21 07:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api_app", "0030_pluginconfig_repositories"),
    ]

    operations = [
        migrations.AddIndex(
            model_name="job",
            index=models.Index(
                fields=["playbook_to_execute", "finished_analysis_time", "user"],
                name="PlaybookConfigOrdering",
            ),
        ),
    ]