import json
import sys

# List of forbidden licenses (add more as needed)
forbidden_licenses = {
    "gpl-1.0", "gpl-2.0", "gpl-3.0",
    "agpl-3.0", "lgpl-2.1", "lgpl-3.0",
    "sspl-1.0"
}

# Load scan result
with open("axios-scan.json", "r", encoding="utf-8") as f:
    data = json.load(f)

found = set()

# Check for forbidden licenses
for file in data.get("files", []):
    for license in file.get("licenses", []):
        key = license.get("key", "")
        if key in forbidden_licenses:
            found.add(key)

if found:
    print("❌ Forbidden licenses found:", ", ".join(found))
    sys.exit(1)

print("✅ No forbidden licenses found.")
