# Generated by Django 3.1.7 on 2021-03-26 16:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SiteComplaint',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('phone', models.IntegerField()),
                ('subject', models.CharField(max_length=266)),
                ('details', models.CharField(max_length=1000)),
                ('website', models.CharField(max_length=100)),
                ('email', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portal.email')),
            ],
        ),
    ]