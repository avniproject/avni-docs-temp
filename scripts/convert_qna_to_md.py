#!/usr/bin/env python3
"""
Convert QnA from CSV to markdown format with specified separator.
"""

import csv
import os
from pathlib import Path

def convert_qna_to_md(csv_file, output_file):
    """
    Convert QnA from CSV to markdown format with separator.
    
    Args:
        csv_file (str): Path to input CSV file
        output_file (str): Path to output markdown file
    """
    try:
        # Ensure output directory exists
        output_path = Path(output_file)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        
        with open(csv_file, 'r', encoding='utf-8') as csvfile, \
             open(output_file, 'w', encoding='utf-8') as md_file:
            
            # Read CSV
            csv_reader = csv.DictReader(csvfile)
            
            # Normalize field names by stripping whitespace
            fieldnames = [f.strip() for f in csv_reader.fieldnames]
            
            # Check if required columns exist
            if 'Question' not in fieldnames or 'Answer' not in fieldnames:
                print("Error: CSV must contain 'Question' and 'Answer' columns")
                print(f"Found columns: {fieldnames}")
                return False
            
            # Process each QnA pair
            for row in csv_reader:
                # Use the original field names from the file
                question = row['Question'].strip()
                # Handle the space after 'Answer' in the header
                answer_key = next((k for k in row.keys() if k.strip() == 'Answer'), None)
                if not answer_key:
                    print("Error: Could not find 'Answer' column in CSV")
                    return False
                    
                answer = row[answer_key].strip()
                
                # Write question (as header)
                md_file.write(f"## {question}\n\n")
                
                # Write answer with proper line breaks for markdown
                # Split into sentences and join with double newlines for better readability
                sentences = [s.strip() for s in answer.split('. ') if s.strip()]
                formatted_answer = '. \n\n'.join(sentences)
                if not formatted_answer.endswith('.'):
                    formatted_answer += '.'
                md_file.write(f"{formatted_answer}\n\n")
                
                # Add separator
                md_file.write("#---#\n\n")
            
            print(f"✓ Successfully converted {csv_reader.line_num - 1} QnA pairs to {output_file}")
            return True
            
    except FileNotFoundError:
        print(f"Error: File not found - {csv_file}")
    except Exception as e:
        print(f"Error processing file: {str(e)}")
    
    return False

if __name__ == "__main__":
    # Define paths
    script_dir = Path(__file__).parent
    repo_root = script_dir.parent
    
    input_csv = repo_root / "qna.csv"
    output_md = repo_root / "test-prompts.md"
    
    # Run conversion
    if input_csv.exists():
        convert_qna_to_md(input_csv, output_md)
    else:
        print(f"Error: Input file not found at {input_csv}")
