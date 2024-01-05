# Generated by Django 4.2.7 on 2024-01-03 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('g_time', '0002_alter_customuser_salaire'),
    ]

    operations = [
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('admin', 'Admin'), ('supervisor', 'Supervisor'), ('employee', 'Employee')], default='employee', max_length=50)),
            ],
        ),
    ]