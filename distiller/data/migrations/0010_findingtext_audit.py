# Generated by Django 3.0.2 on 2020-02-03 17:10

import compositefk.fields
from django.db import migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0009_auto_20200131_2153'),
    ]

    operations = [
        migrations.AddField(
            model_name='findingtext',
            name='audit',
            field=compositefk.fields.CompositeForeignKey(default=None, null_if_equal=[], on_delete=django.db.models.deletion.DO_NOTHING, related_name='finding_texts', to='data.Audit', to_fields={'audit_year': compositefk.fields.LocalFieldValue('audit_year'), 'dbkey': compositefk.fields.LocalFieldValue('dbkey')}),
            preserve_default=False,
        ),
    ]
