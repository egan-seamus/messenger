# Generated by Django 3.1.6 on 2021-02-18 17:23

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('user_id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('username', models.CharField(default='', max_length=100)),
                ('password', models.CharField(default='', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('message_id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('text', models.CharField(default='', max_length=5000)),
                ('timestamp', models.DateTimeField(default=datetime.datetime(1970, 1, 1, 0, 0))),
                ('recipient', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='recipient', to='messaging.customuser')),
                ('sender', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='sender', to='messaging.customuser')),
            ],
        ),
    ]
