import json
from datetime import datetime

# Open a JSON data file
try:
    with open('data_updated_null.json', 'r') as f:
        data = json.load(f)

except json.JSONDecodeError as exc:
    print(f"Error decoding JSON: {exc}")
    exit()

# Look for all fields "updated" and replace them with the current date and time in ISO 8601 format
for item in data:
    if 'updated' in item:
        item['updated'] = datetime.utcnow().isoformat()

# Save the changed data to the data_updated file
with open('data_updated', 'w') as f:
    json.dump(data, f, indent=4)
