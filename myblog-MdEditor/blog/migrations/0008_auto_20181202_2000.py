# Generated by Django 2.0 on 2018-12-02 12:00

from django.db import migrations
import mdeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20181202_1653'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='content',
            field=mdeditor.fields.MDTextField(),
        ),
    ]
