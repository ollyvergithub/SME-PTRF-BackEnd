# Generated by Django 2.2.10 on 2020-10-01 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0100_auto_20201001_0959'),
    ]

    operations = [
        migrations.AddField(
            model_name='prestacaoconta',
            name='ressalvas_aprovacao',
            field=models.TextField(blank=True, default='', verbose_name='Ressalvas na aprovação pela DRE'),
        ),
    ]