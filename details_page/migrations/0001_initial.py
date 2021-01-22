# Generated by Django 3.1.5 on 2021-01-22 08:23

import details_page.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Building',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Namen des Bauwerks eingeben (max. 100 Zeichen).', max_length=100)),
                ('description', models.TextField(blank=True, help_text='Beschreibung des Gebäudes angeben (max. 1000 Zeichen', max_length=1000, null=True)),
                ('city', models.CharField(blank=True, help_text='Stadt des Bauweks eingeben (max. 100 Zeichen).', max_length=100, null=True)),
                ('region', models.CharField(blank=True, help_text='Region des Bauwerks eingeben (max. 100 Zeichen).', max_length=100, null=True)),
                ('country', models.CharField(blank=True, choices=[('Afghanistan', 'AF - Afghanistan'), ('Åland', 'AX - Åland'), ('Albanien', 'AL - Albanien'), ('Algerien', 'DZ - Algerien'), ('Amerikanisch-Samoa', 'AS - Amerikanisch-Samoa'), ('Andorra', 'AD - Andorra'), ('Angola', 'AO - Angola'), ('Anguilla', 'AI - Anguilla'), ('Antarktis', 'AQ - Antarktis'), ('Antigua und Barbuda', 'AG - Antigua und Barbuda'), ('Argentinien', 'AR - Argentinien'), ('Armenien', 'AM - Armenien'), ('Aruba', 'AW - Aruba'), ('Australien', 'AU - Australien'), ('Österreich', 'AT - Österreich'), ('Aserbaidschan', 'AZ - Aserbaidschan'), ('Bahamas', 'BS - Bahamas'), ('Bahrain', 'BH - Bahrain'), ('Bangladesch', 'BD - Bangladesch'), ('Barbados', 'BB - Barbados'), ('Weißrussland', 'BY - Weißrussland'), ('Belgien', 'BE - Belgien'), ('Belize', 'BZ - Belize'), ('Benin', 'BJ - Benin'), ('Bermuda', 'BM - Bermuda'), ('Bhutan', 'BT - Bhutan'), ('Bolivien', 'BO - Bolivien'), ('Bonaire, Sint Eustatius und Saba', 'BQ - Bonaire, Sint Eustatius und Saba'), ('Bosnien und Herzegowina', 'BA - Bosnien und Herzegowina'), ('Botswana', 'BW - Botswana'), ('Bouvetinsel', 'BV - Bouvetinsel'), ('Brasilien', 'BR - Brasilien'), ('Britisches Territorium im Indischen Ozean', 'IO - Britisches Territorium im Indischen Ozean'), ('Britische Jungferninseln', 'VG - Britische Jungferninseln'), ('Brunei', 'BN - Brunei'), ('Bulgarien', 'BG - Bulgarien'), ('Burkina Faso', 'BF - Burkina Faso'), ('Burundi', 'BI - Burundi'), ('Kambodscha', 'KH - Kambodscha'), ('Kamerun', 'CM - Kamerun'), ('Kanada', 'CA - Kanada'), ('Kap Verde', 'CV - Kap Verde'), ('Kaimaninseln', 'KY - Kaimaninseln'), ('Zentralafrikanische Republik', 'CF - Zentralafrikanische Republik'), ('Tschad', 'TD - Tschad'), ('Chile', 'CL - Chile'), ('China', 'CN - China'), ('Weihnachtsinsel', 'CX - Weihnachtsinsel'), ('Kokosinseln', 'CC - Kokosinseln'), ('Kolumbien', 'CO - Kolumbien'), ('Komoren', 'KM - Komoren'), ('Cookinseln', 'CK - Cookinseln'), ('Costa Rica', 'CR - Costa Rica'), ('Kroatien', 'HR - Kroatien'), ('Kuba', 'CU - Kuba'), ('Curacao', 'CW - Curacao'), ('Zypern', 'CY - Zypern'), ('Tschechische Republik', 'CZ - Tschechische Republik'), ('Demokratische Republik Kongo', 'CD - Demokratische Republik Kongo'), ('Dänemark', 'DK - Dänemark'), ('Dschibuti', 'DJ - Dschibuti'), ('Dominica', 'DM - Dominica'), ('Dominikanische Republik', 'DO - Dominikanische Republik'), ('Osttimor', 'TL - Osttimor'), ('Ecuador', 'EC - Ecuador'), ('Ägypten', 'EG - Ägypten'), ('El Salvador', 'SV - El Salvador'), ('Äquatorialguinea', 'GQ - Äquatorialguinea'), ('Eritrea', 'ER - Eritrea'), ('Estland', 'EE - Estland'), ('Äthiopien', 'ET - Äthiopien'), ('Falkland-Inseln', 'FK - Falkland-Inseln'), ('Färöer-Inseln', 'FO - Färöer-Inseln'), ('Fidschi', 'FJ - Fidschi'), ('Finnland', 'FI - Finnland'), ('Frankreich', 'FR - Frankreich'), ('Französisch-Guayana', 'GF - Französisch-Guayana'), ('Französisch-Polynesien', 'PF - Französisch-Polynesien'), ('Französische Süd- und Antarktisgebiete', 'TF - Französische Süd- und Antarktisgebiete'), ('Gabun', 'GA - Gabun'), ('Gambia', 'GM - Gambia'), ('Georgien', 'GE - Georgien'), ('Deutschland', 'DE - Deutschland'), ('Ghana', 'GH - Ghana'), ('Gibraltar', 'GI - Gibraltar'), ('Griechenland', 'GR - Griechenland'), ('Grönland', 'GL - Grönland'), ('Grenada', 'GD - Grenada'), ('Guadeloupe', 'GP - Guadeloupe'), ('Guam', 'GU - Guam'), ('Guatemala', 'GT - Guatemala'), ('Guernsey', 'GG - Guernsey'), ('Guinea', 'GN - Guinea'), ('Guinea-Bissau', 'GW - Guinea-Bissau'), ('Guyana', 'GY - Guyana'), ('Haiti', 'HT - Haiti'), ('Heard und McDonaldinseln', 'HM - Heard und McDonaldinseln'), ('Honduras', 'HN - Honduras'), ('Hongkong', 'HK - Hongkong'), ('Ungarn', 'HU - Ungarn'), ('Island', 'IS - Island'), ('Indien', 'IN - Indien'), ('Indonesien', 'ID - Indonesien'), ('Iran', 'IR - Iran'), ('Irak', 'IQ - Irak'), ('Irland', 'IE - Irland'), ('Isle of Man', 'IM - Isle of Man'), ('Israel', 'IL - Israel'), ('Italien', 'IT - Italien'), ('Elfenbeinküste', 'CI - Elfenbeinküste'), ('Jamaika', 'JM - Jamaika'), ('Japan', 'JP - Japan'), ('Jersey', 'JE - Jersey'), ('Jordanien', 'JO - Jordanien'), ('Kasachstan', 'KZ - Kasachstan'), ('Kenia', 'KE - Kenia'), ('Kiribati', 'KI - Kiribati'), ('Kosovo', 'XK - Kosovo'), ('Kuwait', 'KW - Kuwait'), ('Kirgisistan', 'KG - Kirgisistan'), ('Laos', 'LA - Laos'), ('Lettland', 'LV - Lettland'), ('Libanon', 'LB - Libanon'), ('Lesotho', 'LS - Lesotho'), ('Liberia', 'LR - Liberia'), ('Libyen', 'LY - Libyen'), ('Liechtenstein', 'LI - Liechtenstein'), ('Litauen', 'LT - Litauen'), ('Luxemburg', 'LU - Luxemburg'), ('Macao', 'MO - Macao'), ('Mazedonien', 'MK - Mazedonien'), ('Madagaskar', 'MG - Madagaskar'), ('Malawi', 'MW - Malawi'), ('Malaysia', 'MY - Malaysia'), ('Malediven', 'MV - Malediven'), ('Mali', 'ML - Mali'), ('Malta', 'MT - Malta'), ('Marshallinseln', 'MH - Marshallinseln'), ('Martinique', 'MQ - Martinique'), ('Mauretanien', 'MR - Mauretanien'), ('Mauritius', 'MU - Mauritius'), ('Mayotte', 'YT - Mayotte'), ('Mexiko', 'MX - Mexiko'), ('Mikronesien', 'FM - Mikronesien'), ('Moldawien', 'MD - Moldawien'), ('Monaco', 'MC - Monaco'), ('Mongolei', 'MN - Mongolei'), ('Montenegro', 'ME - Montenegro'), ('Montserrat', 'MS - Montserrat'), ('Marokko', 'MA - Marokko'), ('Mosambik', 'MZ - Mosambik'), ('Myanmar', 'MM - Myanmar'), ('Namibia', 'NA - Namibia'), ('Nauru', 'NR - Nauru'), ('Nepal', 'NP - Nepal'), ('Niederlande', 'NL - Niederlande'), ('Niederländische Antillen', 'AN - Niederländische Antillen'), ('Neukaledonien', 'NC - Neukaledonien'), ('Neuseeland', 'NZ - Neuseeland'), ('Nicaragua', 'NI - Nicaragua'), ('Niger', 'NE - Niger'), ('Nigeria', 'NG - Nigeria'), ('Niue', 'NU - Niue'), ('Norfolkinsel', 'NF - Norfolkinsel'), ('Nordkorea', 'KP - Nordkorea'), ('Nördliche Marianen', 'MP - Nördliche Marianen'), ('Norwegen', 'NO - Norwegen'), ('Oman', 'OM - Oman'), ('Pakistan', 'PK - Pakistan'), ('Palau', 'PW - Palau'), ('Palästinensische Autonomiegebiete', 'PS - Palästinensische Autonomiegebiete'), ('Panama', 'PA - Panama'), ('Papua-Neuguinea', 'PG - Papua-Neuguinea'), ('Paraguay', 'PY - Paraguay'), ('Peru', 'PE - Peru'), ('Philippinen', 'PH - Philippinen'), ('Pitcairninseln', 'PN - Pitcairninseln'), ('Polen', 'PL - Polen'), ('Portugal', 'PT - Portugal'), ('Puerto Rico', 'PR - Puerto Rico'), ('Katar', 'QA - Katar'), ('Republik Kongo', 'CG - Republik Kongo'), ('Réunion', 'RE - Réunion'), ('Rumänien', 'RO - Rumänien'), ('Russland', 'RU - Russland'), ('Ruanda', 'RW - Ruanda'), ('Saint-Barthélemy', 'BL - Saint-Barthélemy'), ('St. Helena', 'SH - St. Helena'), ('St. Kitts und Nevis', 'KN - St. Kitts und Nevis'), ('St. Lucia', 'LC - St. Lucia'), ('St. Martin', 'MF - St. Martin'), ('Saint-Pierre und Miquelon', 'PM - Saint-Pierre und Miquelon'), ('St. Vincent und die Grenadinen', 'VC - St. Vincent und die Grenadinen'), ('Samoa', 'WS - Samoa'), ('San Marino', 'SM - San Marino'), ('São Tomé und Príncipe', 'ST - São Tomé und Príncipe'), ('Saudi-Arabien', 'SA - Saudi-Arabien'), ('Senegal', 'SN - Senegal'), ('Serbien', 'RS - Serbien'), ('Serbien und Montenegro', 'CS - Serbien und Montenegro'), ('Seychellen', 'SC - Seychellen'), ('Sierra Leone', 'SL - Sierra Leone'), ('Singapur', 'SG - Singapur'), ('Sint Maarten', 'SX - Sint Maarten'), ('Slowakei', 'SK - Slowakei'), ('Slowenien', 'SI - Slowenien'), ('Salomon-Inseln', 'SB - Salomon-Inseln'), ('Somalia', 'SO - Somalia'), ('Südafrika', 'ZA - Südafrika'), ('Südgeorgien und die Südlichen Sandwichinseln', 'GS - Südgeorgien und die Südlichen Sandwichinseln'), ('Südkorea', 'KR - Südkorea'), ('Südsudan', 'SS - Südsudan'), ('Spanien', 'ES - Spanien'), ('Sri Lanka', 'LK - Sri Lanka'), ('Sudan', 'SD - Sudan'), ('Suriname', 'SR - Suriname'), ('Svalbard und Jan Mayen', 'SJ - Svalbard und Jan Mayen'), ('Swasiland', 'SZ - Swasiland'), ('Schweden', 'SE - Schweden'), ('Schweiz', 'CH - Schweiz'), ('Syrien', 'SY - Syrien'), ('Taiwan', 'TW - Taiwan'), ('Tadschikistan', 'TJ - Tadschikistan'), ('Tansania', 'TZ - Tansania'), ('Thailand', 'TH - Thailand'), ('Togo', 'TG - Togo'), ('Tokelau', 'TK - Tokelau'), ('Tonga', 'TO - Tonga'), ('Trinidad und Tobago', 'TT - Trinidad und Tobago'), ('Tunesien', 'TN - Tunesien'), ('Türkei', 'TR - Türkei'), ('Turkmenistan', 'TM - Turkmenistan'), ('Turks- und Caicosinseln', 'TC - Turks- und Caicosinseln'), ('Tuvalu', 'TV - Tuvalu'), ('Amerikanische Jungferninseln', 'VI - Amerikanische Jungferninseln'), ('Uganda', 'UG - Uganda'), ('Ukraine', 'UA - Ukraine'), ('Vereinte Arabische Emirate', 'AE - Vereinte Arabische Emirate'), ('Großbritannien', 'GB - Großbritannien'), ('Vereinigte Staaten von Amerika (USA)', 'US - Vereinigte Staaten von Amerika (USA)'), ('United States Minor Outlying Islands', 'UM - United States Minor Outlying Islands'), ('Uruguay', 'UY - Uruguay'), ('Usbekistan', 'UZ - Usbekistan'), ('Vanuatu', 'VU - Vanuatu'), ('Vatikanstadt', 'VA - Vatikanstadt'), ('Venezuela', 'VE - Venezuela'), ('Vietnam', 'VN - Vietnam'), ('Wallis und Futuna', 'WF - Wallis und Futuna'), ('Westsahara', 'EH - Westsahara'), ('Jemen', 'YE - Jemen'), ('Sambia', 'ZM - Sambia'), ('Simbabwe', 'ZW - Simbabwe')], default='Griechenland', help_text='Hier Land des Bauwerks auswählen (Tipp: Zum Suchen Kürzel \n                               auf der Tastatur eingeben).', max_length=100, null=True)),
                ('date_from', models.PositiveIntegerField(blank=True, help_text='Jahr des Baubeginns eingeben. Wenn nicht gesetzt, erscheint das Gebäude nicht auf der Zeitachse.', null=True)),
                ('date_from_BC_or_AD', models.CharField(blank=True, choices=[('v.Chr.', 'v.Chr.'), ('n.Chr.', 'n.Chr.')], default='v.Chr.', help_text='Jahr des Baubeginns: v.Chr. bzw. n.Chr. auswählen.', max_length=7, null=True)),
                ('date_to', models.PositiveIntegerField(blank=True, help_text='Jahr des Bauendes eingeben.', null=True)),
                ('date_to_BC_or_AD', models.CharField(blank=True, choices=[('v.Chr.', 'v.Chr.'), ('n.Chr.', 'n.Chr.')], default='v.Chr.', help_text='Jahr des Bauendes: v.Chr. bzw. n.Chr. auswählen.', max_length=7, null=True)),
                ('architect', models.CharField(blank=True, help_text='Architekt des Bauwerks eingeben (max. 100 Zeichen).', max_length=100, null=True)),
                ('context', models.CharField(blank=True, help_text='Kontext des Bauwerks eingeben (Haus, Siedlung, öfftl. Platz etc., "\n                                         max. 100 Zeichen)', max_length=100, null=True)),
                ('builder', models.CharField(blank=True, help_text='Bauherren des Bauwerks eingeben (max. 100 Zeichen).', max_length=100, null=True)),
                ('construction_type', models.CharField(blank=True, help_text='Bautyp des Bauwerks eingeben (max. 100 Zeichen).', max_length=100, null=True)),
                ('design', models.CharField(blank=True, help_text='Bauform des Bauwerks angeben. (max. 100 Zeichen)', max_length=100, null=True)),
                ('function', models.CharField(blank=True, help_text='Funktion des Bauwerks eingeben (max. 100 Zeichen).', max_length=100, null=True)),
                ('length', models.FloatField(blank=True, help_text='Länge des Bauwerks eingeben (falls vorhanden, in m).', null=True)),
                ('width', models.FloatField(blank=True, help_text='Breite des Bauwerks eingeben (falls vorhanden, in m).', null=True)),
                ('height', models.FloatField(blank=True, help_text='Höhe des Bauwerks eingeben (falls vorhanden, in m).', null=True)),
                ('circumference', models.FloatField(blank=True, help_text='Durchmesser des Bauwerks eingeben (falls vorhanden).', null=True)),
                ('area', models.FloatField(blank=True, help_text='Fläche des Bauwerks eingeben (falls vorhanden, in m²).', null=True)),
                ('column_order', models.CharField(blank=True, help_text='Säulenordnung des Gebäudes eingeben (max. 100 Zeichen).', max_length=100, null=True)),
                ('construction', models.CharField(blank=True, help_text='Konstruktion des Bauwerks eingeben (z.B. Massivbau, etc., falls \n                                    vorhanden, max. 100 Zeichen)', max_length=100, null=True)),
                ('material', models.CharField(blank=True, help_text='Material des Bauwerks eingeben (max. 100 Zeichen).', max_length=100, null=True)),
                ('literature', models.TextField(blank=True, help_text='Literatur zum Gebäude angeben (max. 1000 Zeichen).', max_length=1000, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Era',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('Bronzezeit', 'Bronzezeit'), ('Frühzeit', 'Frühzeit'), ('Archaik', 'Archaik'), ('Klassik', 'Klassik'), ('Helenismus', 'Helenismus'), ('Königszeit', 'Königszeit'), ('Republik', 'Republik'), ('Frühe Kaiserzeit', 'Frühe Kaiserzeit'), ('Mittlere Kaiserzeit', 'Mittlere Kaiserzeit'), ('Späte Kaiserzeit', 'Späte Kaiserzeit'), ('Spätantike', 'Spätantike'), ('Sonstiges', 'Sonstiges')], default='Sonstigedes', help_text='Epoche auswählen', max_length=100)),
                ('year_from', models.PositiveIntegerField(blank=True, help_text='Jahr des Beginns der Epoche eingeben.', null=True)),
                ('year_from_BC_or_AD', models.CharField(blank=True, choices=[('v.Chr.', 'v.Chr.'), ('n.Chr.', 'n.Chr.')], default='v.Chr.', help_text='Jahr des Beginns: v.Chr. bzw. n.Chr. auswählen.', max_length=7, null=True)),
                ('year_to', models.PositiveIntegerField(blank=True, help_text='Jahr des Endes der Epoche eingeben.', null=True)),
                ('year_to_BC_or_AD', models.CharField(blank=True, choices=[('v.Chr.', 'v.Chr.'), ('n.Chr.', 'n.Chr.')], default='v.Chr.', help_text='Jahr des Endes: v.Chr. bzw. n.Chr. auswählen.', max_length=7, null=True)),
                ('visible_on_video_page', models.BooleanField(default=True, help_text="Angeben ob die Epoche auf der 'Staffeln' \n                                                Seite sichtbar sein soll.")),
                ('color_code', models.CharField(default='ffffff', help_text="Hier 6. stelligen Hex-Farbcode für die Epoche eingeben \n                                                             (ohne das führende '#')(z.B.: #ffffff = Weiß).", max_length=6, validators=[details_page.models.validate_color_code])),
            ],
        ),
        migrations.CreateModel(
            name='Picture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Titel des Bildes eingeben (max. 100 Zeichen).', max_length=100)),
                ('description', models.TextField(blank=True, help_text='Beschreibung des Bildes eingeben (max. 1000 Zeichen).', max_length=1000, null=True)),
                ('picture', models.ImageField(height_field='height', help_text='Auf "Durchsuchen" drücken um ein Bild hochzuladen.', upload_to='pics/', width_field='width')),
                ('width', models.IntegerField(default=0, editable=False)),
                ('height', models.IntegerField(default=0, editable=False)),
                ('usable_as_thumbnail', models.BooleanField(default=False, help_text='Anwählen wenn das Bild als Thumbnail (Vorschaubild) für sein \n                                              Bauwerk in der Zeitachse, der Bauwerke-Seite, und in den Suchergebnissen \n                                              erscheinen darf. Bei mehreren möglichen Vorschaubildern für ein Bauwerk \n                                              wird zufällig eins ausgewählt.')),
                ('building', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='details_page.building')),
            ],
        ),
        migrations.AddField(
            model_name='building',
            name='era',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='details_page.era'),
        ),
        migrations.CreateModel(
            name='Blueprint',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Titel des Bauplans eingeben (max. 100 Zeichen).', max_length=100)),
                ('description', models.TextField(blank=True, help_text='Beschreibung des Bildes eingeben (max. 1000 Zeichen).', max_length=1000, null=True)),
                ('blueprint', models.ImageField(height_field='height', help_text='Auf "Durchsuchen" drücken um einen Bauplan hochzuladen.', upload_to='blueprint/', width_field='width')),
                ('width', models.IntegerField(default=0, editable=False)),
                ('height', models.IntegerField(default=0, editable=False)),
                ('building', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='details_page.building')),
            ],
        ),
    ]
