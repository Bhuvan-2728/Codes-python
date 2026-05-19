# file_organizer.py — Auto File Sorter
from pathlib import Path
import shutil

CATEGORIES = {
    "Images"    : [".jpg",".jpeg",".png",".gif",".webp",".svg"],
    "Videos"    : [".mp4",".mov",".avi",".mkv"],
    "Audio"     : [".mp3",".wav",".flac",".aac"],
    "Documents" : [".pdf",".docx",".xlsx",".pptx",".txt",".csv"],
    "Code"      : [".py",".js",".html",".css",".java",".cpp"],
    "Archives"  : [".zip",".tar",".gz",".rar"],
}

def categorize(ext):
    ext = ext.lower()
    for cat, exts in CATEGORIES.items():
        if ext in exts: return cat
    return "Others"

def organize(folder: str, dry_run=False):
    src = Path(folder)
    moved = 0
    for f in src.iterdir():
        if f.is_file():
            cat = categorize(f.suffix)
            dest_dir = src / cat
            print(f"  {'[DRY]' if dry_run else 'MOVE'}: {f.name} → {cat}/")
            if not dry_run:
                dest_dir.mkdir(exist_ok=True)
                shutil.move(str(f), str(dest_dir / f.name))
            moved += 1
    print(f"\n{'Would move' if dry_run else 'Moved'} {moved} file(s).")

def main():
    folder = input("Folder path to organize: ").strip() or "."
    preview = input("Preview only? (y/n): ").lower() == 'y'
    organize(folder, dry_run=preview)

if __name__ == "__main__": main()