import sys

path = "/usr/lib/python3.12/site-packages/modbus_proxy.py"

with open(path, "r") as f:
    content = f.read()

original = content

# Fix 1: reply[6] IndexError
content = content.replace(
    "uid = reply[6]",
    "uid = reply[6] if len(reply) > 6 else 0"
)

# Fix 2: unconditional yaml import — make it a lazy import inside the function
content = content.replace(
    "    import yaml\n",
    "    try:\n        import yaml\n    except ImportError:\n        import json as yaml\n"
)

if content == original:
    print("WARNING: no patterns found to patch", file=sys.stderr)
else:
    with open(path, "w") as f:
        f.write(content)
    print("Patch applied successfully")
