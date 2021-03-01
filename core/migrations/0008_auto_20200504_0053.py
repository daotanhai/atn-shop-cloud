# Generated by Django

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_item_color_label'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='color_label',
            field=models.CharField(choices=[('R', 'red'), ('BLU', 'blue'), ('YEL', 'yellow'), ('BL', 'black'), ('OR', 'orange')], max_length=10),
        ),
    ]
