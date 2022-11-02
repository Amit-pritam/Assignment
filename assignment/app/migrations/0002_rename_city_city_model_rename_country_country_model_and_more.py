# Generated by Django 4.1.2 on 2022-11-01 21:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='City',
            new_name='City_Model',
        ),
        migrations.RenameModel(
            old_name='Country',
            new_name='Country_Model',
        ),
        migrations.RenameModel(
            old_name='Location',
            new_name='Location_Model',
        ),
        migrations.RenameModel(
            old_name='State',
            new_name='State_Model',
        ),
        migrations.CreateModel(
            name='UserData_Model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Country_name', models.ManyToManyField(to='app.country_model')),
                ('city_name', models.ManyToManyField(to='app.city_model')),
                ('location_name', models.ManyToManyField(to='app.location_model')),
                ('state_name', models.ManyToManyField(to='app.state_model')),
            ],
        ),
    ]