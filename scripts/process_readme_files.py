#!/usr/bin/env python3
"""
Script to process all markdown files in the readme directory.
Removes the first 12 lines but keeps the second and third lines (title and excerpt).
"""

import os
import glob
from pathlib import Path

def process_file(file_path):
    """
    Process a single markdown file by:
    1. Keeping lines 2 and 3 (title and excerpt)
    2. Removing lines 1, 4-12
    3. Keeping all content from line 13 onwards
    """
    try:
        # Read the file
        with open(file_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        
        if len(lines) < 13:
            print(f"Warning: {file_path} has fewer than 13 lines. Skipping...")
            return False
        
        # Create new content: lines 2, 3, and 13+
        new_lines = []
        
        # Add lines 2 and 3 (index 1 and 2)
        if len(lines) > 1:
            new_lines.append(lines[1])  # line 2 (title)
        if len(lines) > 2:
            new_lines.append(lines[2])  # line 3 (excerpt)
        
        # Add all lines from 13 onwards (index 12+)
        new_lines.extend(lines[12:])
        
        # Write the modified content back to the file
        with open(file_path, 'w', encoding='utf-8') as f:
            f.writelines(new_lines)
        
        print(f"✓ Processed: {file_path}")
        return True
        
    except Exception as e:
        print(f"✗ Error processing {file_path}: {str(e)}")
        return False

def main():
    """Main function to process all markdown files in the readme directory."""
    
    # Get the script directory and find the readme directory
    script_dir = Path(__file__).parent
    readme_dir = script_dir.parent / "readme"
    
    if not readme_dir.exists():
        print(f"Error: readme directory not found at {readme_dir}")
        return
    
    print(f"Processing markdown files in: {readme_dir}")
    print("-" * 50)
    
    # Find all markdown files recursively
    pattern = str(readme_dir / "**" / "*.md")
    md_files = glob.glob(pattern, recursive=True)
    
    if not md_files:
        print("No markdown files found in the readme directory.")
        return
    
    print(f"Found {len(md_files)} markdown files to process...")
    print()
    
    # Process each file
    processed_count = 0
    failed_count = 0
    
    for file_path in sorted(md_files):
        if process_file(file_path):
            processed_count += 1
        else:
            failed_count += 1
    
    print()
    print("-" * 50)
    print(f"Processing complete!")
    print(f"✓ Successfully processed: {processed_count} files")
    if failed_count > 0:
        print(f"✗ Failed to process: {failed_count} files")
    
    # Show what the transformation does
    print()
    print("Transformation applied:")
    print("- Kept line 2 (title)")
    print("- Kept line 3 (excerpt)")
    print("- Removed lines 1, 4-12 (YAML front matter)")
    print("- Kept all content from original line 13 onwards")

if __name__ == "__main__":
    main()
