# Generated by Django 2.2.10 on 2020-04-29 22:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_user_associacao'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='associacao',
        ),
    ]
