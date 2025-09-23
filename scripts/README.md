# README File Processing Scripts

This directory contains scripts to process markdown files in the `readme` directory by removing YAML front matter while preserving title and excerpt information.

## Scripts Overview

### 1. `process_readme_files.py` - Main Processing Script
**Purpose**: Processes all markdown files in the readme directory by removing the first 12 lines but keeping lines 2 and 3.

**What it does**:
- Keeps line 2 (title)
- Keeps line 3 (excerpt) 
- Removes lines 1, 4-12 (YAML front matter)
- Keeps all content from original line 13 onwards

**Usage**:
```bash
cd scripts
python3 process_readme_files.py
```

### 2. `backup_readme_files.py` - Backup Script
**Purpose**: Creates timestamped backups of all markdown files before processing.

**Usage**:
```bash
cd scripts
python3 backup_readme_files.py
```

### 3. `test_single_file.py` - Test Script
**Purpose**: Tests the transformation on a single file to verify the logic before running on all files.

**Usage**:
```bash
cd scripts
python3 test_single_file.py
```

## Recommended Workflow

1. **Create Backup** (recommended):
   ```bash
   python3 backup_readme_files.py
   ```

2. **Test on Single File** (optional but recommended):
   ```bash
   python3 test_single_file.py
   ```

3. **Process All Files**:
   ```bash
   python3 process_readme_files.py
   ```

## Example Transformation

**Before** (original file):
```markdown
---
title: 'How to guide: Setting up Locations via CSV Upload'
excerpt: For bulk location upload after Release 10.0
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
## Definitions

Below is a list of definitions...
```

**After** (processed file):
```markdown
title: 'How to guide: Setting up Locations via CSV Upload'
excerpt: For bulk location upload after Release 10.0
## Definitions

Below is a list of definitions...
```

## Safety Features

- **Backup Script**: Creates timestamped backups before processing
- **Test Script**: Allows testing on a single file first
- **Error Handling**: Scripts handle errors gracefully and report issues
- **File Validation**: Checks if files have enough lines before processing
- **Progress Reporting**: Shows detailed progress and results

## File Structure

```
scripts/
├── README.md                    # This file
├── process_readme_files.py      # Main processing script
├── backup_readme_files.py       # Backup creation script
├── test_single_file.py          # Single file test script
└── readme_backup_YYYYMMDD_HHMMSS/  # Backup directories (created when needed)
```

## Notes

- All scripts are designed to work from the `scripts` directory
- The scripts automatically find the `readme` directory relative to their location
- Processing is recursive - it finds all `.md` files in subdirectories
- Scripts preserve file encoding (UTF-8) and line endings
- Error reporting shows which files failed to process (if any)
