# Generated by Django 3.2.6 on 2021-08-17 22:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('learning_logs', '0002_entry'),
    ]

    operations = [
        migrations.RenameField(
            model_name='topic',
            old_name='date_added',
            new_name='data_added',
        ),
    ]
