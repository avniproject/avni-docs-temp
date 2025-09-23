#!/usr/bin/env python3
"""
Test script to verify the transformation on a single file.
This creates a copy of a file and shows the before/after comparison.
"""

import os
import shutil
from pathlib import Path

def show_file_preview(file_path, title, max_lines=20):
    """Show a preview of the file content."""
    print(f"\n{title}")
    print("=" * len(title))
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        
        for i, line in enumerate(lines[:max_lines], 1):
            print(f"{i:2d}: {line.rstrip()}")
        
        if len(lines) > max_lines:
            print(f"... ({len(lines) - max_lines} more lines)")
            
    except Exception as e:
        print(f"Error reading file: {e}")

def process_file_copy(original_path, copy_path):
    """Process the copy of the file with the same logic as the main script."""
    try:
        # Read the file
        with open(copy_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        
        if len(lines) < 13:
            print(f"Warning: File has fewer than 13 lines.")
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
        with open(copy_path, 'w', encoding='utf-8') as f:
            f.writelines(new_lines)
        
        return True
        
    except Exception as e:
        print(f"Error processing file: {e}")
        return False

def main():
    """Test the transformation on a single file."""
    
    # Use the currently open file as test subject
    test_file = "/Users/vinay/code/avni/avni-docs-temp/readme/End User Guide/how-to-guide-setting-up-locations-via-csv-upload.md"
    
    if not Path(test_file).exists():
        print(f"Test file not found: {test_file}")
        return
    
    # Create a copy for testing
    script_dir = Path(__file__).parent
    test_copy = script_dir / "test_file_copy.md"
    
    try:
        # Copy the original file
        shutil.copy2(test_file, test_copy)
        
        # Show original content
        show_file_preview(test_file, "ORIGINAL FILE CONTENT")
        
        # Process the copy
        if process_file_copy(test_file, test_copy):
            # Show processed content
            show_file_preview(test_copy, "PROCESSED FILE CONTENT")
            
            print(f"\n✓ Test completed successfully!")
            print(f"Original file: {test_file}")
            print(f"Test copy: {test_copy}")
            print("\nTransformation summary:")
            print("- Kept line 2 (title)")
            print("- Kept line 3 (excerpt)")  
            print("- Removed lines 1, 4-12")
            print("- Kept all content from original line 13+")
        else:
            print("✗ Test failed!")
            
    except Exception as e:
        print(f"Error during test: {e}")
    
    finally:
        # Clean up test copy
        if test_copy.exists():
            test_copy.unlink()
            print(f"\nCleaned up test file: {test_copy}")

if __name__ == "__main__":
    main()
