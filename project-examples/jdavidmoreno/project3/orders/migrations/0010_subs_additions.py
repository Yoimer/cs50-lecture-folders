# Generated by Django 2.0.3 on 2018-08-01 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0009_auto_20180731_1507'),
    ]

    operations = [
        migrations.AddField(
            model_name='subs',
            name='additions',
            field=models.ManyToManyField(blank=True, related_name='subs', to='orders.Additions'),
        ),
    ]
