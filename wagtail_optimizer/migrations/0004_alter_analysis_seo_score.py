# Generated by Django 5.0.1 on 2024-10-01 20:13

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wagtail_optimizer', '0003_alter_analysis_options_analysis_seo_score'),
    ]

    operations = [
        migrations.AlterField(
            model_name='analysis',
            name='seo_score',
            field=models.DecimalField(decimal_places=2, default=100, max_digits=5, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)], verbose_name='SEO Score'),
        ),
    ]
