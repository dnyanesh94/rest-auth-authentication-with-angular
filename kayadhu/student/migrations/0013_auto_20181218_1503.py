# Generated by Django 2.1.4 on 2018-12-18 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0012_auto_20181217_1150'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentcontact',
            name='contact_type',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
