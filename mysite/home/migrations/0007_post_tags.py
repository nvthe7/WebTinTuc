# Generated by Django 2.2.1 on 2019-05-15 01:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_auto_20190514_1655'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='Tags',
            field=models.CharField(default='netnews', max_length=500),
        ),
    ]
