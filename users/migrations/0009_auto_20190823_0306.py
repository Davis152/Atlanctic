# Generated by Django 2.1.11 on 2019-08-23 06:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_auto_20190823_0128'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='typeuser',
            field=models.CharField(choices=[(1, 'Candidates'), (2, 'Employer')], max_length=10, null=True, verbose_name='Type User'),
        ),
    ]
