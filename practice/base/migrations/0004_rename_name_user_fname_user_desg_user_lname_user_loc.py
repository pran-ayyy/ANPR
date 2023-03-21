# Generated by Django 4.0.5 on 2023-01-13 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_alter_log_options_remove_user_groups_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='name',
            new_name='fname',
        ),
        migrations.AddField(
            model_name='user',
            name='desg',
            field=models.CharField(default='Emp', max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='lname',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='loc',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
