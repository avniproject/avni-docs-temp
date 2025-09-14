import os
import glob

# ---- Part 1 removed: no Google Sheet export ----

# ---- Part 2: Merge all Markdown files in repo (including subfolders) ----

repo_path = "."  # Current directory (your repo root)

# Find all markdown files recursively
md_files = glob.glob(os.path.join(repo_path, "**", "*.md"), recursive=True)

# Exclude merged.md and test-prompts.md
excluded_files = {"merged.md", "test-prompts.md"}
md_files = [f for f in md_files if os.path.basename(f) not in excluded_files]

# Sort them for consistency
md_files.sort()

with open("merged.md", "w", encoding="utf-8") as outfile:
    for fname in md_files:
        outfile.write(f"\n\n# File: {fname}\n\n")
        with open(fname, "r", encoding="utf-8") as infile:
            outfile.write(infile.read())

print(f"✅ Merged {len(md_files)} Markdown files (excluding test-prompts.md) into merged.md")
