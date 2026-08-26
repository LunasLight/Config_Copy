"""
ConfigCopy.py

Version 1.2
Author: LunasLight

This script will copy all the folders, configs and presets while
retaining folder structure into a new directory with only
the configs and presets for SPTushonka mods

Reasons this exists: Sending configs to a friend, updating SPT while retaining configs,
backing up configs if you have to delete mods for any reason, all without keeping the mod
downloaded thus saving on disk space (It's 2026 storage is expensive)

Usage: Place the script into SPTushonka Root folder and run it, the output will be under the "!Script_Output" folder
(Technically it will work as long as it's ran in any folder that is a parent of the mods you're trying to copy from)
"""

# import os
import shutil
import glob
from pathlib import Path

# file_path = Path(__file__).resolve()
DIR_PATH = Path.cwd()
OUT_DIR = Path(DIR_PATH / "!Config_Copy_Output")
CONFIG_REGEX = "/**/*[C]onfig*.json*"
PRESET_REGEX = "/**/*[P]reset*/*.json*"


def main():
    """Main Function"""
    directory_create()
    configs_copied = file_copy("Config", CONFIG_REGEX)
    presets_copied = file_copy("Preset", PRESET_REGEX)
    print(
        f"Copied a total of '{configs_copied}' configs and '{presets_copied}' presets"
    )


def file_copy(filetype, regex):
    """Copies the regex matched files (.json*)"""
    files_copied = 0
    for file in glob.iglob(str(DIR_PATH) + regex, recursive=True):
        mods_location = Path(file).parts.index(DIR_PATH.parts[-1])
        cleaned_list = Path(file).parts[mods_location + 1 : -1]
        final_dir = Path(OUT_DIR / Path(*cleaned_list))
        final_dir.mkdir(parents=True, exist_ok=True)
        shutil.copy(file, final_dir)
        files_copied += 1
        print(f"{filetype} Copied: {file}")

    return files_copied


def directory_create():
    """Creates / Replaces the output path"""
    if not OUT_DIR.exists():
        OUT_DIR.mkdir(parents=False, exist_ok=False)
    else:
        shutil.rmtree(OUT_DIR)
        OUT_DIR.mkdir(parents=False, exist_ok=False)


if __name__ == "__main__":
    main()
