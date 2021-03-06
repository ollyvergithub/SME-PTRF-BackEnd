# Generated by Django 2.2.10 on 2020-08-24 13:12

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('dre', '0006_auto_20200819_0720'),
    ]

    operations = [
        migrations.CreateModel(
            name='FaqCategoria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criado_em', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('alterado_em', models.DateTimeField(auto_now=True, verbose_name='Alterado em')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('nome', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name': 'Faq - Categoria',
                'verbose_name_plural': 'Faqs - Categorias',
            },
        ),
    ]
