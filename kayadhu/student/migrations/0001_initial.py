# Generated by Django 2.1.4 on 2018-12-11 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('middle_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('birth_date', models.DateField()),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], default='M', max_length=1)),
                ('blood_group', models.CharField(max_length=3)),
                ('caste', models.CharField(max_length=50)),
                ('religion', models.CharField(max_length=50)),
                ('birth_place', models.CharField(max_length=50)),
                ('identification_mark', models.TextField()),
            ],
        ),
    ]
