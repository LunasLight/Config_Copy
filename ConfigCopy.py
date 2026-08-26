"""
ConfigCopy.py

This script will copy all the folders, configs and presets while
retaining folder structure into a new directory with only
the configs and presets for SPTushonka mods

Reasons this exists: Sending configs to a friend, updating SPT while retaining configs,
backing up configs if you have to delete mods for any reason, all without keeping the mod
downloaded thus saving on disk space (It's 2026 storage is expensive)

Usage: Place the script into SPT_Runtime/user/mods (SPT/user/mods for other versions)
and run it, the output will be under the "!Script_Output" folder
"""

import os
import re
import shutil
import glob
from pathlib import Path

# file_path = os.path.abspath(__file__)
# dir_path = Path(os.path.dirname(file_path))
file_path = Path(__file__).resolve()
dir_path = Path.cwd()
r_path = r"^.*?" + str(dir_path)
out_path = dir_path / "!Script_Output"
folders_created = 0
configs_found = 0
directories_checked = 0


def main():
    directory_create()
    print("Copied a total of " + str(directory_copy()) + " configs")
    # print(Path.cwd())
    """print(
        "The current file path is: "
        + str(file_path)
        + "\nand has "
        + str(directories)
        + " folders."
    ) """


def directory_copy():
    # global directories_checked
    global configs_found
    # for path in Path.cwd().iterdir():
    # directories_checked += 1
    # print("TEST" + str(dir_path))
    for config in glob.iglob(str(dir_path) + "/**/*config*.json*", recursive=True):
        # os.mkdir("!Script_Output" / path)
        configs_found += 1
        mods_location = Path(config).parts.index(dir_path.parts[-1])
        cleaned_list = Path(config).parts[mods_location + 1 : -1]
        # print(cleaned_list)
        final_path = out_path / Path(*cleaned_list)
        # final_path = out_path + Path(cleaned_list)
        # print(final_path)
        os.makedirs(final_path, exist_ok=True)
        shutil.copy(config, final_path)
        # test3 = Path(config).parts[test2 + 1 : -1]
        # test5 = Path(config).parts.index("mods")[1:-1]
        # test4 = Path(config).parts["mods" + 1 : -1]
        # print("THIS IS TEST 4 " + str(test4))
        # print("THIS IS TEST 5 " + str(test5))
        # print("THIS IS TEST 3" + str(test3))
        """buffer_path = Path(config)
        print(buffer_path.parts)
        n = buffer_path.parts.index("mods")
        # del buffer_path.parts[:n]
        print(buffer_path.parts[n + 1:])
        clean_list = buffer_path.parts[n + 1 : -1]
        print(clean_list)"""
        # os.makedirs(Path(config[:1]))
        # os.makedirs("!Script_Output" / clean_list)
        # os.makedirs("!Script_Output" / clean_list)
        # subfolders = re.sub(r_path, str(dir_path), config)
        #  print(str(subfolders))
        # shutil.copyfile(config, out_path / "aaa/")
        # shutil.copytree(config, out_path)
        print("Copied: " + str(config))
    # for preset in glob.iglob(str(dir_path) + "/*preset*/*", recursive=True): print(str(preset))
    return configs_found


def directory_create():
    if not os.path.exists(dir_path / "!Script_Output"):
        os.mkdir("!Script_Output")
    else:
        shutil.rmtree(dir_path / "!Script_Output")
        os.mkdir("!Script_Output")
    # for path in Path.cwd().iterdir():


def find_configs():
    pass


if __name__ == "__main__":
    main()
