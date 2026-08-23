import os
import sys
import time


def human_size(num_bytes):
    units = ["B", "KB", "MB", "GB", "TB", "PB"]
    size = float(num_bytes)
    for unit in units:
        if size < 1000 or unit == units[-1]:
            if unit == "B":
                return f"{int(size)} B"
            return f"{size:.2f} {unit}"
        size /= 1000


def measure(root):
    start = time.time()
    last_update = start
    files = 0
    dirs = 0
    total_bytes = 0
    errors = 0
    showed_progress = False
    stack = [root]

    while stack:
        current = stack.pop()
        try:
            entries = os.scandir(current)
        except OSError:
            errors += 1
            continue
        with entries:
            for entry in entries:
                try:
                    if entry.is_dir(follow_symlinks=False):
                        dirs += 1
                        stack.append(entry.path)
                    elif entry.is_file(follow_symlinks=False):
                        st = entry.stat(follow_symlinks=False)
                        files += 1
                        total_bytes += st.st_size
                except OSError:
                    errors += 1
                    continue

                now = time.time()
                if now - last_update >= 5:
                    mins, secs = divmod(int(now - start), 60)
                    print(
                        f"\rCounting... {files:,} files, "
                        f"{human_size(total_bytes)}, {mins}:{secs:02d} elapsed",
                        end="",
                        flush=True,
                    )
                    showed_progress = True
                    last_update = now

    return files, dirs, total_bytes, errors, time.time() - start, showed_progress


def print_report(clean, files, dirs, total_bytes, errors, elapsed):
    mins, secs = divmod(int(elapsed), 60)
    print(f"Folder:      {clean}")
    print(f"Total size:  {human_size(total_bytes)}")
    print(f"Files:       {files:,}")
    print(f"Folders:     {dirs:,}")
    print(f"Time taken:  {mins}:{secs:02d}")
    if elapsed > 0 and files:
        print(f"Speed:       {files / elapsed:,.0f} files per second")
    if errors:
        print(f"Skipped (no permission): {errors:,}")
    print()


def main():
    args = sys.argv[1:]
    if not args:
        print("This tool measures how big folders are, including everything inside.")
        print()
        print("Easiest way to use it:")
        print("  1. Type:  python3  then a space (don't press Enter yet)")
        print("  2. Drag this script into the Terminal window")
        print("  3. Type another space")
        print("  4. Drag in the folder you want measured")
        print("  5. Press Enter")
        sys.exit(1)

    grand_files = 0
    grand_bytes = 0

    for i, path in enumerate(args):
        clean = path.rstrip("/")
        if not os.path.isdir(clean):
            print("That path doesn't exist, or it isn't a folder:")
            print(f"  {path}")
            print("Tip: drag the folder in from Finder instead of typing it.")
            sys.exit(1)

        if len(args) > 1:
            print(f"[{i + 1} of {len(args)}]")

        files, dirs, total_bytes, errors, elapsed, showed_progress = measure(clean)
        if showed_progress:
            print("\r" + " " * 79 + "\r", end="")
        print_report(clean, files, dirs, total_bytes, errors, elapsed)

        grand_files += files
        grand_bytes += total_bytes

    if len(args) > 1:
        print("-" * 40)
        print(
            f"All folders combined: {human_size(grand_bytes)} "
            f"across {grand_files:,} files"
        )


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print()
        print("Stopped early. Nothing was changed on your drive.")
        sys.exit(130)
