import requests
from collections import Counter

# Overpass API URL
url = "http://overpass-api.de/api/interpreter"

# Overpass query
query = """
[out:json];
area["name"="Berlin"]->.searchArea;
(
  way["highway"]["name"](area.searchArea);
);
out body;
>;
out skel qt;
"""

# Send request to Overpass API
response = requests.get(url, params={'data': query})
data = response.json()

# Extract street names and highway types
streets_by_highway = {}
for element in data['elements']:
    if 'tags' in element and 'name' in element['tags'] and 'highway' in element['tags']:
        highway_type = element['tags']['highway']
        street_name = element['tags']['name']
        if highway_type not in streets_by_highway:
            streets_by_highway[highway_type] = []
        streets_by_highway[highway_type].append(street_name)

# Log the number of total streets after extraction
total_streets = sum(len(streets) for streets in streets_by_highway.values())
print(f"Total streets extracted: {total_streets}")

# Log the number of streets by highway type
for highway_type, street_names in streets_by_highway.items():
    print(f"Highway type: {highway_type}, Streets: {len(street_names)}")

# Log the top ten most common street names
all_street_names = [name for names in streets_by_highway.values() for name in names]
name_counts = Counter(all_street_names)
top_ten_names = name_counts.most_common(10)
print("\nTop ten most common street names:")
for name, count in top_ten_names:
    print(f"{name}: {count}")

# Aggregate and count street names by highway type
for highway_type, street_names in streets_by_highway.items():
    print(f"\nHighway type: {highway_type}")
    name_counts = Counter(street_names)
    duplicate_streets = {name: count for name, count in name_counts.items() if count > 1}
    
    # Log the number of total streets after filtering duplicates
    print(f"Total streets after filtering duplicates: {len(duplicate_streets)}")

    # Output top ten most common street names for each highway type
    print(f"Top ten most common {highway_type} names:")
    for name, count in name_counts.most_common(10):
        print(f"{name}: {count}")
