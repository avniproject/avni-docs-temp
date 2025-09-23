#!/usr/bin/env python3
"""
Script to create backups of all markdown files in the readme directory
before processing them.
"""

import os
import shutil
import glob
from pathlib import Path
from datetime import datetime

def main():
    """Create backups of all markdown files in the readme directory."""
    
    # Get the script directory and find the readme directory
    script_dir = Path(__file__).parent
    readme_dir = script_dir.parent / "readme"
    
    if not readme_dir.exists():
        print(f"Error: readme directory not found at {readme_dir}")
        return
    
    # Create backup directory with timestamp
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_dir = script_dir / f"readme_backup_{timestamp}"
    backup_dir.mkdir(exist_ok=True)
    
    print(f"Creating backup in: {backup_dir}")
    print("-" * 50)
    
    # Find all markdown files recursively
    pattern = str(readme_dir / "**" / "*.md")
    md_files = glob.glob(pattern, recursive=True)
    
    if not md_files:
        print("No markdown files found in the readme directory.")
        return
    
    print(f"Found {len(md_files)} markdown files to backup...")
    print()
    
    # Copy each file maintaining directory structure
    backup_count = 0
    
    for file_path in sorted(md_files):
        try:
            # Calculate relative path from readme directory
            rel_path = Path(file_path).relative_to(readme_dir)
            
            # Create destination path in backup directory
            dest_path = backup_dir / rel_path
            
            # Create parent directories if they don't exist
            dest_path.parent.mkdir(parents=True, exist_ok=True)
            
            # Copy the file
            shutil.copy2(file_path, dest_path)
            
            print(f"✓ Backed up: {rel_path}")
            backup_count += 1
            
        except Exception as e:
            print(f"✗ Error backing up {file_path}: {str(e)}")
    
    print()
    print("-" * 50)
    print(f"Backup complete!")
    print(f"✓ Successfully backed up: {backup_count} files")
    print(f"Backup location: {backup_dir}")

if __name__ == "__main__":
    main()
