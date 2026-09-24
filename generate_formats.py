from pathlib import Path

SINE_MOD_LOCATION = Path(r"C:\Users\anthony.maxwell\AppData\Roaming\zen\Profiles\x7rsjsz9.Default (release)\chrome\sine-mods\34c7fedd-aaf8-4194-99bf-ab52692299ed")

import json, shutil

with open("config.json", "r") as f:
    config = json.load(f)
    with open("config.css", "w") as f:
        f.writelines([":root {"] + [f"--{var}: {value if not isinstance(value, list) else ', '.join(value)};" for var, value in config.items()] + ["}"])

shutil.copy("config.css", SINE_MOD_LOCATION / "zen/config.css")
