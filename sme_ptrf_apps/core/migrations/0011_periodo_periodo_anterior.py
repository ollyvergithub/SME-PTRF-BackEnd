# Generated by Django 2.2.10 on 2020-04-15 16:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_auto_20200414_1541'),
    ]

    operations = [
        migrations.AddField(
            model_name='periodo',
            name='periodo_anterior',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='periodo_seguinte', to='core.Periodo'),
        ),
    ]
