"""
Config_Copy.py

Version 1.3.2
Author: LunasLight
Website: https://github.com/LunasLight/Config_Copy

This script will copy all the folders, configs and presets while
retaining folder structure into a new directory with only
said configs and presets for SPTushonka mods

Usage: Place the script into SPTushonka Root folder and run it, the output will be under the "!Config_Copy_Output" folder
(Technically it will work as long as it's ran in any folder that is a parent of the mods you're trying to copy/backup from)

E.g: py .\\Config_Copy.py
"""

import shutil
from pathlib import Path
from time import perf_counter_ns

DIR_PATH = Path.cwd()
OUT_DIR = Path(DIR_PATH / "!Config_Copy_Output")
CONFIG_REGEX = "*Config*.json*"
PRESET_REGEX = "*Preset*/*.json*"


def main():
    """Main Function"""
    directory_create()
    start = perf_counter_ns()
    configs_copied = file_copy("Config", CONFIG_REGEX)
    presets_copied = file_copy("Preset", PRESET_REGEX)
    stop = perf_counter_ns()
    print(
        f"\nCopied a total of {configs_copied} configs and {presets_copied} presets in"
        f" {(stop - start) / 1e6:.1f} ms or {(stop - start) / 1e9:.3f} seconds"
    )


def directory_create():
    """Creates / Replaces the output path"""
    if not OUT_DIR.exists():
        OUT_DIR.mkdir(parents=False, exist_ok=False)
    else:
        shutil.rmtree(OUT_DIR)
        OUT_DIR.mkdir(parents=False, exist_ok=False)


def file_copy(filetype, regex):
    """Copies the regex matched files (.json*) with path.rglob"""
    files_copied = 0
    location = DIR_PATH.parts.index(DIR_PATH.parts[-1])
    for file in DIR_PATH.rglob(regex, case_sensitive=False):
        # If the file path contains any exclamation point at the start of any directory it's skipped
        if not file.full_match("**/!*/**"):
            file_out_dir = OUT_DIR / Path(*file.parts[location + 1 : -1])
            file_out_dir.mkdir(parents=True, exist_ok=True)
            shutil.copy(file, file_out_dir)
            files_copied += 1
            print(f"{filetype} Copied: {file}")
    return files_copied


if __name__ == "__main__":
    main()
