import csv
import os
import re

INPUT = "artwork.csv"
OUTPUT_DIR = "markdown"
os.makedirs(OUTPUT_DIR, exist_ok=True)

def slugify(text):
    return re.sub(r'-+', '-', re.sub(r'[^a-z0-9]+', '-', text.lower())).strip('-') or "untitled"

with open(INPUT, newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for index, row in enumerate(reader):
        title = row.get("title", "").strip()
        line = row.get("line", "").strip()
        description = row.get("description", "").strip()
        artists = row.get("artists", "").strip()

        slug = slugify(title)
        filename = f"{slug}.md"
        filepath = os.path.join(OUTPUT_DIR, filename)

        with open(filepath, "w", encoding="utf-8") as mdfile:
            mdfile.write(f"---\n")
            mdfile.write(f"tags: post\n")
            mdfile.write(f"title: \"{title}\"\n")
            mdfile.write(f"line: \"{line}\"\n")
            mdfile.write(f"artists: \"{artists}\"\n")
            mdfile.write(f"---\n\n")
            mdfile.write(description)

        print(f"✅ Created {filename}")
