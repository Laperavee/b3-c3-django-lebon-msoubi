# Generated by Django 4.1.12 on 2024-01-21 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_alter_password_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='password',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
