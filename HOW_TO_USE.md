# How to use folder_size.py

## Before your first run

Every Mac already includes Python, so there's nothing to install. However, the very first time you ever run anything with `python3`, macOS may pop up a message asking to install "Command Line Developer Tools". If that happens, click Install, let it finish (a few minutes), then start again from step 1 below.

## Running it, step by step

1. Open Terminal: press Cmd + Space, type `terminal`, press Enter.
2. Type `python3` followed by one space. Do not press Enter yet.
3. Find `folder_size.py` in Finder (in this folder) and drag it into the Terminal window. You'll see its path appear after `python3 `.
4. Type one more space.
5. Drag in the folder you want measured (i.e. your sample library or backup drive).
6. Press Enter and watch the live counter.
7. When it finishes you get a summary like this:

```
Folder:      /Volumes/T7 Shield/Sample Library
Total size:  2.88 TB
Files:       5,535,850
Folders:     121,280
Time taken:  11:59
Speed:       7,699 files per second
```

A finished command looks like this before you press Enter:

```
python3 /Users/[Username]/folder_size_tool/folder_size.py "/Volumes/T7 Shield/Sample Library"
```

Always drag files in instead of typing paths. Folder names with spaces in them will break if typed incorrectly, and dragging the folder straight in gets them right every time.

## Reading the results

- **Total size** is the number Get Info would have given you, if it ever finished...
- **Files** and **Folders** count everything found at any depth
- **Time taken** and **Speed** are there so you can appreciate beating Finder
- **Skipped** means a few spots your account doesn't have permission to read, which is normal on Macs.

## Handy extras

- **Several folders at once:** after dragging in the first folder, add another space and drag in another one. Repeat as many times as you like, then press Enter. Each folder gets its own report plus a combined total at the end.
- **Stop early:** press Control + C. It prints a goodbye note and stops.
- **Works anywhere:** external SSDs, spinning HDDs, USB sticks, any folder. Spinning hard drives are slower than SSDs though, that's normal (but not as slow as finder using Get Info).

## If something goes wrong

- **Popup about Command Line Developer Tools:** click Install, wait, try again. Happens once.
- **"That path doesn't exist":** the folder path got mangled, usually from typing it. Clear the line (Cmd + Delete works) and drag the folder in from Finder instead.
- **Nothing seems to happen:** on giant folders the counter updates every 5 seconds, give it a moment.
- **Numbers look stuck near the end:** macOS caches listings, so re-running the same folder later is always much faster than the first time.
