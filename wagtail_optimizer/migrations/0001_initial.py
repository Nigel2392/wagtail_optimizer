# Generated by Django 5.0.1 on 2024-10-01 19:42

import wagtail_optimizer.json
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Analyis',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('notes', models.TextField(blank=True, null=True)),
                ('multi_page_errors', models.JSONField(blank=True, encoder=wagtail_optimizer.json.WagtailOptimizerJSONEncoder, null=True)),
                ('multi_page_warnings', models.JSONField(blank=True, encoder=wagtail_optimizer.json.WagtailOptimizerJSONEncoder, null=True)),
                ('single_page_errors', models.JSONField(blank=True, encoder=wagtail_optimizer.json.WagtailOptimizerJSONEncoder, null=True)),
                ('single_page_warnings', models.JSONField(blank=True, encoder=wagtail_optimizer.json.WagtailOptimizerJSONEncoder, null=True)),
                ('pages', models.JSONField(blank=True, encoder=wagtail_optimizer.json.ExpandedWagtailOptimizerJSONEncoder, null=True)),
                ('mpe_count', models.IntegerField(default=0, verbose_name='Multi-Page Errors')),
                ('mpw_count', models.IntegerField(default=0, verbose_name='Multi-Page Warnings')),
                ('spe_count', models.IntegerField(default=0, verbose_name='Single-Page Errors')),
                ('spw_count', models.IntegerField(default=0, verbose_name='Single-Page Warnings')),
                ('p_count', models.IntegerField(default=0, verbose_name='Pages Analyzed Count')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
