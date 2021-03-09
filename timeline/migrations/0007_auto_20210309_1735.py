# Generated by Django 3.1.5 on 2021-03-09 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timeline', '0006_auto_20210305_1507'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicdate',
            name='infos',
            field=models.TextField(help_text='Hier eine kurze Beschreibung des historischen Ereignisses einfügen (max. 1000 Zeichen).', max_length=1000, verbose_name='Information'),
        ),
        migrations.AlterField(
            model_name='historicdate',
            name='year_BC_or_AD',
            field=models.CharField(choices=[('v.Chr.', 'v.Chr.'), ('n.Chr.', 'n.Chr.')], default='v.Chr.', help_text='Jahr des Ereignisses: v.Chr. bzw. n.Chr. auswählen.', max_length=7, verbose_name='vor oder nach Christigeburt?'),
        ),
    ]
