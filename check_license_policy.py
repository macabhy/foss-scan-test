import json

# Define forbidden licenses
FORBIDDEN_LICENSES = {"gpl-3.0", "gpl-2.0", "agpl-3.0"}

# Load ScanCode JSON
with open("reports/axios-scan.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# Collect all license keys
license_keys = set()
for file in data.get("files", []):
    for lic in file.get("licenses", []):
        key = lic.get("spdx_license_key")
        if key:
            license_keys.add(key.lower())

# Compare against policy
forbidden_found = license_keys.intersection(FORBIDDEN_LICENSES)

# Build output summary
if forbidden_found:
    print("❌ Forbidden licenses found:")
    for lic in sorted(forbidden_found):
        print(f" - {lic}")
else:
    print("✅ No forbidden licenses found.")

if license_keys:
    print(f"\n🏷️ Detected licenses: {', '.join(sorted(license_keys))}")
else:
    print("⚠️ No licenses detected.")
