import re, sys

path = "/usr/lib/python3.12/site-packages/modbus_proxy.py"

with open(path, "r") as f:
    content = f.read()

patched = content.replace(
    "uid = reply[6]",
    "uid = reply[6] if len(reply) > 6 else 0"
)

if patched == content:
    print("ERROR: pattern not found, patch failed!", file=sys.stderr)
    sys.exit(1)

with open(path, "w") as f:
    f.write(patched)

print("Patch applied successfully")
