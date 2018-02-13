# Generated by Django 2.0.2 on 2018-02-06 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scorer', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='paper',
            name='body',
        ),
        migrations.RemoveField(
            model_name='paper',
            name='title',
        ),
        migrations.AlterField(
            model_name='paper',
            name='stance',
            field=models.CharField(help_text='Stance of Title in relation to Body', max_length=20, null=True),
        ),
    ]