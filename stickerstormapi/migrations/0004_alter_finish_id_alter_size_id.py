# Generated by Django 5.0.1 on 2024-01-28 22:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stickerstormapi', '0003_alter_sticker_finish_type_alter_sticker_sticker_size'),
    ]

    operations = [
        migrations.AlterField(
            model_name='finish',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='size',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
