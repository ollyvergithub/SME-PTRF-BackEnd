# Generated by Django 2.2.10 on 2021-01-07 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('receitas', '0029_tiporeceita_e_recursos_proprios'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tiporeceita',
            name='e_recursos_proprios',
            field=models.BooleanField(default=False, verbose_name='Recursos Externos'),
        ),
    ]
