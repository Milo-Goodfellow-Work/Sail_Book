# Generated by Django 3.0.8 on 2020-07-10 19:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0005_auto_20200710_1554'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='secret_token',
            field=models.CharField(default='-Wxl6S50AXQl5h3WnIPaw1EI8N-MBg', max_length=22),
        ),
    ]
