# Generated by Django 3.1.6 on 2021-02-12 01:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('messaging', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='password',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='customuser',
            name='user_id',
            field=models.BigIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='customuser',
            name='username',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='message',
            name='text',
            field=models.CharField(default='', max_length=5000),
        ),
    ]