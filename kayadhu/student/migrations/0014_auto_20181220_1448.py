# Generated by Django 2.0.8 on 2018-12-20 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0013_auto_20181218_1503'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentimage',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='student/profile/images'),
        ),
    ]
