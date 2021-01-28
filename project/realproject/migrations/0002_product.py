# Generated by Django 3.1.4 on 2020-12-31 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realproject', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=50)),
                ('price', models.CharField(max_length=50)),
                ('upload_date', models.DateField(blank=True, null=True)),
            ],
        ),
    ]