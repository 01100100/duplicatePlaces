# duplicatePlaces

Tiny python script to find OSM places with the same name within a Region using Overpass API.

Note: This does not validate or clean the data extracted from OSM, the goal is to list different places with the same name, however there are many cases where you have more then 1 Osm elements representing a place. This causes duplicates in the output which intefers with the results.

## Quick Start

```bash
git clone git@github.com:01100100/duplicatePlaces.git
cd duplicatePlaces
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python duplicatePlaces.py
```

## Output

```bash
Total streets extracted: 67700
Highway type: residential, Streets: 30007
Highway type: primary, Streets: 4114
Highway type: secondary, Streets: 11152
Highway type: living_street, Streets: 2054
Highway type: tertiary, Streets: 6653
Highway type: service, Streets: 5336
Highway type: unclassified, Streets: 957
Highway type: footway, Streets: 3893
Highway type: motorway_link, Streets: 27
Highway type: trunk, Streets: 129
Highway type: path, Streets: 637
Highway type: secondary_link, Streets: 147
Highway type: track, Streets: 840
Highway type: motorway, Streets: 52
Highway type: pedestrian, Streets: 372
Highway type: primary_link, Streets: 87
Highway type: construction, Streets: 217
Highway type: tertiary_link, Streets: 35
Highway type: cycleway, Streets: 148
Highway type: steps, Streets: 138
Highway type: trunk_link, Streets: 10
Highway type: busway, Streets: 2
Highway type: corridor, Streets: 18
Highway type: bridleway, Streets: 4
Highway type: proposed, Streets: 47
Highway type: platform, Streets: 614
Highway type: elevator, Streets: 6
Highway type: services, Streets: 1
Highway type: road, Streets: 2
Highway type: bus_stop, Streets: 1

Top ten most common street names:
Hauptstraße: 296
Landsberger Allee: 274
Märkische Allee: 208
Berliner Straße: 193
Heerstraße: 179
Sonnenallee: 170
Allee der Kosmonauten: 168
Karl-Marx-Straße: 151
Frankfurter Allee: 146
Bundesallee: 146

Highway type: residential
Total streets after filtering duplicates: 5046
Top ten most common residential names:
Heerstraße: 58
Weserstraße: 56
Charlottenstraße: 54
Waldstraße: 51
Allee der Kosmonauten: 51
Hauptstraße: 50
Dorfstraße: 49
Eisenacher Straße: 46
Lehrter Straße: 45
Gartenstraße: 42

Highway type: primary
Total streets after filtering duplicates: 166
Top ten most common primary names:
Landsberger Allee: 207
Märkische Allee: 135
Tempelhofer Damm: 112
Müllerstraße: 107
Frankfurter Allee: 104
Potsdamer Straße: 101
Seestraße: 99
Heerstraße: 96
Danziger Straße: 96
Martin-Luther-Straße: 83

Highway type: secondary
Total streets after filtering duplicates: 558
Top ten most common secondary names:
Sonnenallee: 166
Karl-Marx-Straße: 146
Hermannstraße: 127
Kurfürstendamm: 117
Hohenzollerndamm: 114
Allee der Kosmonauten: 113
Berliner Straße: 109
Hauptstraße: 105
Bundesallee: 97
Blumberger Damm: 97

Highway type: living_street
Total streets after filtering duplicates: 399
Top ten most common living_street names:
Dahlemer Weg: 38
Zwieseler Straße: 22
Schönwalder Allee: 21
Ceciliengärten: 20
Malteserstraße: 20
Malplaquetstraße: 14
Wrangelstraße: 14
Planufer: 14
Sigmaringer Straße: 13
Seeadlerweg: 13

Highway type: tertiary
Total streets after filtering duplicates: 639
Top ten most common tertiary names:
Südwestkorso: 56
Rubensstraße: 51
Kiefholzstraße: 50
Fritz-Erler-Allee: 50
Friedenstraße: 49
Schloßstraße: 48
Werbellinstraße: 47
Wiesbadener Straße: 45
Birkbuschstraße: 44
Gottlieb-Dunkel-Straße: 42

Highway type: service
Total streets after filtering duplicates: 1094
Top ten most common service names:
Wolfener Straße: 54
Schwarzer Weg: 32
Hauptweg: 31
Hauptstraße: 29
Sewanstraße: 28
Salvador-Allende-Straße: 26
Rummelsburger Straße: 23
Grenzweg: 21
Zur Nachtheide: 20
Sterndamm: 19

Highway type: unclassified
Total streets after filtering duplicates: 191
Top ten most common unclassified names:
Nennhauser Damm: 23
Wendenschloßstraße: 23
Quickborner Straße: 17
Heerstraße: 13
Treuenbrietzener Straße: 12
Dannenwalder Weg: 12
Fürstendamm: 11
Hauptstraße: 11
Zufahrt zum Flughafen Tegel: 10
Colditzstraße: 10

Highway type: footway
Total streets after filtering duplicates: 693
Top ten most common footway names:
Rosenweg: 74
Fliederweg: 41
Hauptweg: 39
Dahlienweg: 37
Asternweg: 34
Nelkenweg: 31
Tulpenweg: 28
Mittelweg: 22
Amselweg: 22
Bellevueallee: 20

Highway type: motorway_link
Total streets after filtering duplicates: 3
Top ten most common motorway_link names:
AVUS: 17
Gottlieb-Dunkel-Brücke: 4
Buschkrugallee: 2
Kurt-Schumacher-Damm: 1
Schildhornstraße: 1
Gradestraße: 1
AVUS Nordkurve: 1

Highway type: trunk
Total streets after filtering duplicates: 10
Top ten most common trunk names:
Berlin Turnpike: 30
Tunnel Tiergarten Spreebogen: 22
Spindlersfelder Straße: 21
Worcester Highway: 16
West White Horse Pike: 10
Ocean Gateway: 10
South White Horse Pike: 8
White Horse Pike: 4
U.S. Route 2: 4
Wilhelm-Spindler-Brücke: 2

Highway type: path
Total streets after filtering duplicates: 119
Top ten most common path names:
Havelhöhenweg: 21
Hochspannungsweg: 12
Eichgestell: 11
Schöneberger Schleife: 11
Paul-Schwarz-Promenade: 10
Vinetaplatz: 9
Carl-Zuckmayer-Brücke: 9
Hansakorso: 8
Goerdelersteg: 7
Alexander-von-Humboldt-Weg: 7

Highway type: secondary_link
Total streets after filtering duplicates: 21
Top ten most common secondary_link names:
Bundesplatz: 22
Bundesallee: 15
Schloßstraße: 10
Alt-Friedrichsfelde: 7
Daumstraße: 5
Wilhelmstraße: 5
Buckower Damm: 5
Rhinstraße: 4
Karolinenstraße: 4
Masurenallee: 3

Highway type: track
Total streets after filtering duplicates: 169
Top ten most common track names:
Schwarzer Weg: 22
Hauptgestell: 16
Rosenweg: 10
Königsweg: 9
Birkenweg: 9
Schildower Weg: 9
Fischerhüttenweg: 8
Winterweg: 8
Verlängerter Sandbacher Weg: 7
Mittelweg: 7

Highway type: motorway
Total streets after filtering duplicates: 2
Top ten most common motorway names:
AVUS: 45
Tunnel Schlangenbader Straße: 6
Hinckeldeybrücke: 1

Highway type: pedestrian
Total streets after filtering duplicates: 61
Top ten most common pedestrian names:
Greenwichpromenade: 24
Wilmersdorfer Straße: 18
Pepitapromenade: 10
Anton-Saefkow-Platz: 8
Marzahner Promenade: 8
Alt-Tegel: 7
Frieda-Arnheim-Promenade: 7
Steinmetzstraße: 6
Neue Promenade: 6
Propststraße: 6

Highway type: primary_link
Total streets after filtering duplicates: 14
Top ten most common primary_link names:
Märkische Allee: 18
Unter den Eichen: 10
Gensinger Straße: 8
Landsberger Allee: 7
Alt-Friedrichsfelde: 6
Schnellerstraße: 3
Wuhletalstraße: 3
Piesporter Straße: 3
Mehringdamm: 3
Lichtenrader Damm: 3

Highway type: construction
Total streets after filtering duplicates: 41
Top ten most common construction names:
Buckower Chaussee: 8
Märkische Allee: 8
Treskowallee: 7
Wegedornstraße: 6
Blumberger Damm: 5
Karl-Marx-Platz: 5
Perleberger Straße: 5
Rathenower Straße: 4
Ostendstraße: 4
Bäkestraße: 3

Highway type: tertiary_link
Total streets after filtering duplicates: 9
Top ten most common tertiary_link names:
Daimlerstraße: 5
Großbeerenstraße: 3
Osdorfer Straße: 3
Werbellinstraße: 3
Südwestkorso: 2
Steglitzer Damm: 2
Rixdorfer Straße: 2
Fritz-Erler-Allee: 2
Komturstraße: 2
Heylstraße: 1

Highway type: cycleway
Total streets after filtering duplicates: 21
Top ten most common cycleway names:
Großer Stern: 28
Jakob-Kaiser-Platz: 22
Togostraße: 6
Prinzregentenstraße: 3
Falckensteinstraße: 3
Dahmeweg: 3
Cross Vermont Trail: 3
Bellermannstraße: 3
Kreuznacher Straße: 2
An der Malche: 2

Highway type: steps
Total streets after filtering duplicates: 18
Top ten most common steps names:
Havelhöhenweg: 12
Sasarsteig: 8
Marzahner Promenade: 4
Mäusetunnel: 4
Kindl-Treppe: 4
Vera-Brittain-Ufer: 4
Elsa-Rendschmidt-Weg: 3
Hechtgraben: 3
Rosenweg: 3
Denkzeichenweg: 2

Highway type: trunk_link
Total streets after filtering duplicates: 1
Top ten most common trunk_link names:
Spindlersfelder Straße: 10

Highway type: busway
Total streets after filtering duplicates: 1
Top ten most common busway names:
Hallesche-Tor-Brücke: 2

Highway type: corridor
Total streets after filtering duplicates: 0
Top ten most common corridor names:
Kaiser Wilhelm Passage: 1
J-Straße: 1
K-Straße: 1
L-Straße: 1
23-Straße: 1
24-Straße: 1
25-Straße: 1
26-Straße: 1
27-Straße: 1
28-Straße: 1

Highway type: bridleway
Total streets after filtering duplicates: 1
Top ten most common bridleway names:
Dahlwitzer Heuweg: 2
Schildower Weg: 1
Hin­der­nis­par­cours: 1

Highway type: proposed
Total streets after filtering duplicates: 5
Top ten most common proposed names:
Blumberger Chaussee: 8
Süd-Ost-Verbindung (SOV): 6
Märkische Allee: 5
Tangentiale Verbindung Ost: 4
Münchehagenstraße: 2
Alexander-Meißner-Straße: 1
Storkower Straße: 1
Gorissenstraße: 1
Tangentiale Verbindung Ost - Kombivariante (in Planung): 1
Am Schloßhof: 1

Highway type: platform
Total streets after filtering duplicates: 223
Top ten most common platform names:
S+U Rathaus Spandau: 10
S+U Zoologischer Garten: 7
Brunsbütteler Damm/Ruhlebener Straße: 6
Am Omnibushof: 6
U Rathaus Reinickendorf: 5
Baumschulenstraße/Königsheideweg: 4
Neuköllner Straße/Zwickauer Damm: 4
U Unter den Linden: 4
Britzer Damm/Gradestraße: 4
Buschkrug: 4

Highway type: elevator
Total streets after filtering duplicates: 2
Top ten most common elevator names:
Aufzug Gleis 1+3: 3
Aufzug Gleis 2+4: 2
U Freie Universität (Thielplatz): 1

Highway type: services
Total streets after filtering duplicates: 0
Top ten most common services names:
Grunewald West: 1

Highway type: road
Total streets after filtering duplicates: 0
Top ten most common road names:
Südstraße: 1
Heinrich-Hertz-Straße: 1

Highway type: bus_stop
Total streets after filtering duplicates: 0
Top ten most common bus_stop names:
Am Rohrgarten: 1
```
