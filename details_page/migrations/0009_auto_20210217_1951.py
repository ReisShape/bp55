# Generated by Django 3.1.5 on 2021-02-17 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('details_page', '0008_building_links'),
    ]

    operations = [
        migrations.AlterField(
            model_name='building',
            name='links',
            field=models.TextField(blank=True, default='', help_text='Weiterführende Links zum Gebäude angeben (max. 1000 Zeichen).', max_length=1000, null=True, verbose_name='Links'),
        ),
        migrations.AlterField(
            model_name='era',
            name='name',
            field=models.CharField(choices=[('Bronzezeit', 'Bronzezeit'), ('Frühe Eisenzeit', 'Frühe Eisenzeit'), ('Archaik', 'Archaik'), ('Königszeit', 'Königszeit'), ('Klassik', 'Klassik'), ('Republik', 'Republik'), ('Hellenismus', 'Hellenismus'), ('Frühe Kaiserzeit', 'Frühe Kaiserzeit'), ('Mittlere Kaiserzeit', 'Mittlere Kaiserzeit'), ('Späte Kaiserzeit', 'Späte Kaiserzeit'), ('Spätantike', 'Spätantike'), ('Sonstiges', 'Sonstiges')], help_text='Epoche auswählen.', max_length=100, unique=True, verbose_name='Name'),
        ),
    ]
