# Generated by Django 2.1.4 on 2018-12-13 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0003_studentimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentimage',
            name='image',
            field=models.TextField(),
        ),
    ]