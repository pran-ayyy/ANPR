# Generated by Django 4.0.5 on 2023-01-13 09:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_rename_name_user_fname_user_desg_user_lname_user_loc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='log',
            name='onduty',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='onduty_user', to='base.user'),
        ),
    ]
