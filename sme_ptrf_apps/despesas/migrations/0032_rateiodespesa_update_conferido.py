# Generated by Django 2.2.10 on 2020-09-09 07:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('despesas', '0031_remove_rateiodespesa_prestacao_conta'),
    ]

    operations = [
        migrations.AddField(
            model_name='rateiodespesa',
            name='update_conferido',
            field=models.BooleanField(default=False, verbose_name='Atualiza conferido?'),
        ),
    ]
