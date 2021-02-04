# Generated by Django 3.1.5 on 2021-02-03 19:23

import details_page.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('details_page', '0003_auto_20210129_1734'),
    ]

    operations = [
        migrations.AlterField(
            model_name='building',
            name='construction',
            field=models.CharField(blank=True, help_text='Konstruktion des Bauwerks eingeben\n                                    (z.B. Massivbau, etc., falls vorhanden, max. 100 Zeichen)', max_length=100, null=True, validators=[details_page.models.validate_url_conform_str]),
        ),
        migrations.AlterField(
            model_name='building',
            name='construction_type',
            field=models.CharField(blank=True, help_text='Bautyp des Bauwerks eingeben (max. 100 Zeichen).', max_length=100, null=True, validators=[details_page.models.validate_url_conform_str]),
        ),
        migrations.AlterField(
            model_name='building',
            name='context',
            field=models.CharField(blank=True, help_text='Kontext des Bauwerks eingeben (Haus, Siedlung,\n                                   öfftl. Platz etc., "max. 100 Zeichen)', max_length=100, null=True, validators=[details_page.models.validate_url_conform_str]),
        ),
        migrations.AlterField(
            model_name='building',
            name='design',
            field=models.CharField(blank=True, help_text='Bauform des Bauwerks angeben. (max. 100 Zeichen)', max_length=100, null=True, validators=[details_page.models.validate_url_conform_str]),
        ),
        migrations.AlterField(
            model_name='building',
            name='name',
            field=models.CharField(help_text='Namen des Bauwerks eingeben (max. 100 Zeichen).', max_length=100, validators=[details_page.models.validate_url_conform_str]),
        ),
        migrations.AlterField(
            model_name='picture',
            name='usable_as_thumbnail',
            field=models.BooleanField(default=False, help_text='Anwählen wenn das Bild als Thumbnail\n                                              (Vorschaubild) für sein Bauwerk in der Zeitachse,\n                                              der Bauwerke-Seite, und in den Suchergebnissen \n                                              erscheinen darf. \n                                              Bei mehreren möglichen Vorschaubildern für ein Bauwerk \n                                              wird zufällig eins ausgewählt.'),
        ),
    ]