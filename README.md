# Folder Size Tool

A simple tool that tells you the size of a folder and how many files are inside it. It does what right-click > Get Info does in Finder, except it doesn't freeze on huge folders.

It only reads listings and sizes. It never changes, moves, or deletes anything on your drives.

Simple tool designed as a time saver.

## Quick start

1. Open Terminal (Cmd + Space, type `terminal`, press Enter).
2. Type `python3` followed by a space (don't press Enter yet).
3. Drag `folder_size.py` from Finder into the Terminal window.
4. Type another space, then drag in the folder you want measured.
5. Press Enter and watch it count away.

Full step-by-step instructions, including what to do if something goes wrong, are in [HOW_TO_USE.md](HOW_TO_USE.md).

## What you'll see

```
Folder:      /Volumes/T7 Shield/Sample Library
Total size:  2.88 TB
Files:       5,535,850
Folders:     121,280
Time taken:  11:59
Speed:       7,699 files per second
```

## Good to know

- **Several folders at once:** drag in more than one before pressing Enter. Each gets its own report plus a combined total at the end.
- **Stop early:** press Control + C. It prints a goodbye note and stops.
- **Skipped:** means that your account doesn't have permission to read something, which is normal on Macs.
- Sizes match Finder and Get Info (TB = 1,000 MB), so numbers line up with the that.

## Requirements

Any Mac. Python is already included, so there is nothing to install. The very first time you run anything with `python3`, macOS may ask to install "Command Line Developer Tools" — click Install once and it never asks again.

## License

[MIT](LICENSE)
