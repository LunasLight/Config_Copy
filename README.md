# THIS IS NOT A MOD. THIS IS A PYTHON SCRIPT

### Overview

## This should work on ANY SPT version that uses config files and presets, I know it says 4.1.3 but that's cause I don't know how to list it for all of them.

## This will quickly copy all the config and preset .json/.jsonc files into 1 directory for you to do with as you please while retaining folder structure as it is on your drive.

### Reasons this exists

* Sending configs to someone without having to dig through a bajillion different folders and paths
* Updating SPT while retaining custom/tweaked configs 
* backing up configs if you have to delete mods for any reason, all without keeping the bulk of the mod downloaded thus saving on disk space (It's 2026 storage is expensive)  

I made this because a friend wanted to get my configs for the fika server we were playing on. I uploaded it here because if I had a use case for it maybe someone else will too. 
  
I Briefly looked around for this specific functionality with different mod managers and none of them (from what I saw) backed up configs and preset files this way so I made this script.

## Prerequisites
A decently up to date python install and basic command line usage (or just follow along with the video at the bottom)

## Usage 
Place the script into the SPTushonka Root folder and run it, the output will be under the directory:  
`/!Config_Copy_Output`  

This should work on ANY SPT version that uses config files and presets, I know it says 4.1.3 but that's cause I don't know how to list it for all of them.

### Step by Step Example
1. Move "Config_Copy.py" into your SPT root directory and open command prompt in the address bar at the top by typing `cmd`  
2. Copy Paste or type the below snippet into your command prompt (Ctrl + Shift + V sometimes)
`py .\Config_Copy.py` Yes it is case sensitive
3. Profit? The newly created `/!Config_Copy_Output`  folder will have all your configs and presets  

(Technically it will work as long as it's ran in any folder that is a parent of the mods you're trying to copy/backup from including `/user/mods/`)

## Video Guide
Here is a step by step video on how to use on my working SPT 4.1.3.  
Probably want to open the full video, the resolution is small in the auto-embed

https://youtu.be/phP0_Xx96XE

## VirusTotal Results
https://www.virustotal.com/gui/file/249da22883f9ff05d716bd06c24e66c28ed773dc089efe4d456935a7d1401749/detection