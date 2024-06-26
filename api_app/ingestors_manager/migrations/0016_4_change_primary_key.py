# Generated by Django 4.2.8 on 2024-01-09 14:31
import django
from django.db import migrations, models


def migrate(apps, schema_editor):
    IngestorReport = apps.get_model("ingestors_manager", "IngestorReport")
    IngestorConfig = apps.get_model("ingestors_manager", "IngestorConfig")
    name = IngestorConfig.objects.filter(
        name=models.OuterRef("old_config")
    ).values_list("pk")[:1]
    IngestorReport.objects.update(config=models.Subquery(name))


class Migration(migrations.Migration):
    dependencies = [
        ("ingestors_manager", "0016_3_change_primary_key"),
    ]

    operations = [
        migrations.RenameField(
            model_name="ingestorreport", old_name="config", new_name="old_config"
        ),
        migrations.AddField(
            model_name="ingestorreport",
            name="config",
            field=models.ForeignKey(
                default=None,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="reports",
                to="ingestors_manager.ingestorconfig",
                null=True,
            ),
            preserve_default=False,
        ),
        migrations.RunPython(migrate),
        migrations.AlterField(
            model_name="ingestorreport",
            name="config",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="reports",
                to="ingestors_manager.ingestorconfig",
            ),
        ),
        migrations.RemoveField(model_name="ingestorreport", name="old_config"),
    ]
