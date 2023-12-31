# Generated by Django 4.2.7 on 2024-01-05 14:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('g_time', '0003_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='role',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='users', to='g_time.role'),
        ),
        migrations.AlterField(
            model_name='role',
            name='name',
            field=models.CharField(choices=[('admin', 'Admin'), ('supervisor', 'Supervisor'), ('employee', 'Employee')], default='employee', max_length=50, unique=True),
        ),
    ]
