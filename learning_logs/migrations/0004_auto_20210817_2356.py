# Generated by Django 3.2.6 on 2021-08-17 23:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('learning_logs', '0003_rename_date_added_topic_data_added'),
    ]

    operations = [
        migrations.RenameField(
            model_name='entry',
            old_name='data_added',
            new_name='date_added',
        ),
        migrations.RenameField(
            model_name='topic',
            old_name='data_added',
            new_name='date_added',
        ),
    ]
