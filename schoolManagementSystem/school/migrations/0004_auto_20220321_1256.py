# Generated by Django 3.2.4 on 2022-03-21 12:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0003_delete_appointment'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Patient',
            new_name='Student',
        ),
        migrations.RenameModel(
            old_name='Doctor',
            new_name='Teacher',
        ),
    ]