# Generated by Django 4.2.8 on 2024-01-09 14:31
import django
from django.db import migrations, models


def migrate(apps, schema_editor):
    PivotConfig = apps.get_model("pivots_manager", "PivotConfig")
    PlaybookConfig = apps.get_model("playbooks_manager", "PlaybookConfig")
    Organization = apps.get_model("certego_saas_organization", "Organization")
    PivotConfig.objects.update(
        playbook_to_execute2=models.Subquery(
            PlaybookConfig.objects.filter(
                name=models.OuterRef("playbook_to_execute")
            ).values_list("pk")[:1]
        ),
    )
    for config in PivotConfig.objects.all():
        if config.disabled2:
            OrganizationPluginConfiguration = apps.get_model(
                "api_app", "OrganizationPluginConfiguration"
            )
            ContentType = apps.get_model("contenttypes", "ContentType")
            ct = ContentType.objects.get_for_model(config)
            for org in config.disabled2:
                if org:
                    OrganizationPluginConfiguration.objects.create(
                        organization=Organization.objects.get(pk=org),
                        object_id=config.pk,
                        content_type=ct,
                        disabled=True,
                    )


class Migration(migrations.Migration):
    dependencies = [
        ("api_app", "0001_2_initial_squashed"),
        ("playbooks_manager", "0024_3_change_primary_key"),
        ("pivots_manager", "0024_2_change_primary_key"),
    ]

    operations = [
        migrations.AlterField(
            model_name="pivotconfig",
            name="playbook_to_execute",
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
        migrations.AddField(
            model_name="pivotconfig",
            name="playbook_to_execute2",
            field=models.ForeignKey(
                default=None,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="executed_by_pivot",
                to="playbooks_manager.playbookconfig",
                null=True,
            ),
            preserve_default=False,
        ),
        migrations.RunPython(
            migrate,
        ),
        migrations.RemoveField(model_name="pivotconfig", name="playbook_to_execute"),
        migrations.RenameField(
            model_name="pivotconfig",
            old_name="playbook_to_execute2",
            new_name="playbook_to_execute",
        ),
        migrations.AlterField(
            model_name="pivotconfig",
            name="playbook_to_execute",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                related_name="executed_by_pivot",
                to="playbooks_manager.playbookconfig",
            ),
        ),
        migrations.RemoveField(model_name="pivotconfig", name="disabled2"),
    ]
