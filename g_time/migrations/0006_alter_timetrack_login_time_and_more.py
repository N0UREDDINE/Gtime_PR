# Generated by Django 4.2.7 on 2024-01-12 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('g_time', '0005_alter_role_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timetrack',
            name='login_time',
            field=models.TimeField(),
        ),
        migrations.AlterField(
            model_name='timetrack',
            name='logout_time',
            field=models.TimeField(blank=True, null=True),
        ),
    ]
