# Generated by Django 3.2.8 on 2021-10-24 11:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0009_remove_module_public'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='module',
            options={'ordering': ['-Created_at']},
        ),
        migrations.RenameField(
            model_name='module',
            old_name='created_at',
            new_name='Created_at',
        ),
        migrations.RenameField(
            model_name='module',
            old_name='description',
            new_name='Description',
        ),
        migrations.RenameField(
            model_name='module',
            old_name='title',
            new_name='Title',
        ),
    ]
