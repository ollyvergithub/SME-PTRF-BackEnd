# Generated by Django 2.2.10 on 2020-05-07 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('receitas', '0005_tiporeceita_e_repasse'),
    ]

    operations = [
        migrations.AddField(
            model_name='receita',
            name='conferido',
            field=models.BooleanField(default=False, verbose_name='Conferido?'),
        ),
    ]