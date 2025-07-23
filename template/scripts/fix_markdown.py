#!/usr/bin/env python3
"""
DOCX to PDF Conversion Pipeline - Markdown Cleanup Script

"""

import re
import sys
import argparse

def process_yaml_block(match):
    """
    Process and clean up YAML frontmatter blocks that have been escaped during DOCX conversion.
    
    Args:
        match (re.Match): Regular expression match object containing the escaped YAML block
        
    Returns:
        str: Cleaned YAML block with proper formatting and removed empty lines
    """
    # Extract the matched YAML content
    yaml_content = match.group(0)
    
    # De-escape YAML block delimiters (\\-\\-- becomes ---)
    # This fixes the opening and closing markers of YAML frontmatter
    yaml_content = re.sub(r'\\-\\--', r'---', yaml_content)
    
    # De-escape hash symbols used for comments in YAML
    yaml_content = re.sub(r'\\#', r'#', yaml_content)
    
    # De-escape quotation marks that may be used in YAML values
    yaml_content = re.sub(r'\\"', r'"', yaml_content)  # Double quotes
    yaml_content = re.sub(r"\\'", r"'", yaml_content)  # Single quotes
    
    # De-escape hyphens used in YAML lists and keys
    yaml_content = re.sub(r'\\-', r'-', yaml_content)
    
    # De-escape underscores that might be used in YAML keys or values
    yaml_content = re.sub(r'\\_', r'_', yaml_content)
    
    # De-escape caret symbols (^) - Note: comment says > but code uses ^
    yaml_content = re.sub(r'\\^', r'^', yaml_content)
    
    # Remove empty lines from YAML block for cleaner formatting
    # This helps ensure the YAML is properly parsed by downstream tools
    yaml_content = "\n".join(line for line in yaml_content.splitlines() if line.strip())
    
    return yaml_content


def process_markdown(input_text):
    """
    Main function to process and clean up markdown text that has conversion artifacts.
    
    Args:
        input_text (str): Raw markdown content with conversion artifacts
        
    Returns:
        str: Cleaned markdown content ready for PDF conversion
    """
    
    # Process YAML frontmatter block first
    # Pattern explanation:
    # (?s) - DOTALL flag, makes . match newlines
    # (\\-\\--\s*\n.*?\n\\-\\--) - Matches escaped YAML block delimiters with content
    yaml_pattern = r"(?s)(\\-\\--\s*\n.*?\n\\-\\--)"
    
    # Apply YAML block processing using the helper function
    text = re.sub(yaml_pattern, process_yaml_block, input_text)
    
    # De-escape @ symbols that appear after whitespace
    # This is common for email addresses or citation formats
    text = re.sub(r' \\@', r' @', text)
    
    # Global de-escaping of quotation marks throughout the document
    # These often get escaped during DOCX conversion and need to be restored
    text = re.sub(r'\\"', r'"', text)  # Double quotes
    text = re.sub(r"\\'", r"'", text)  # Single quotes
   
    # De-escape backticks used for code formatting
    # Backticks are essential for inline code and code blocks in markdown
    text = re.sub(r'\\`', r'`', text)
   
    # De-escape backslashes when they appear before text characters
    # This prevents over-escaping while preserving intentional backslashes
    # Pattern: \\\\([a-zA-Z]) matches double-escaped backslash before letters
    text = re.sub(r'\\\\([a-zA-Z])', r'\\\1', text)
   
    # Fix footnote references that got malformed during conversion
    # Converts patterns like [^\[1\]^](#fn1) to proper [^1] format
    # This regex handles various footnote reference formats that can result from conversion
    text = re.sub(r'\[\^\\?\[(\d+)\\?\]\^](?:\(#fn\d+\))?', r'[^\1]', text)
    
    # Fix citation key formatting for bibliography processing
    # Converts escaped citation patterns like \[@key\] back to [@key]
    # This is crucial for bibliography tools like pandoc-citeproc
    text = re.sub(r"\\\[@(.*?)\\\]", r"[@\1]", text)
   
    # Process footnote content/definitions
    def format_footnote(match):
        """
        Helper function to properly format footnote definitions.
        
        Footnote definitions in markdown should follow the format: [^num]: content
        This function extracts the footnote number and content from malformed
        footnote definitions and reformats them correctly.
        
        Args:
            match (re.Match): Match object containing footnote number and content
            
        Returns:
            str: Properly formatted footnote definition
        """
        num = match.group(1)      # Extract footnote number
        content = match.group(2)  # Extract footnote content
        return f'[^{num}]: {content}'
   
    # Apply footnote formatting to footnote definitions
    # Pattern matches: "1. content (#fnref1)" and converts to "[^1]: content"
    # This handles footnote definitions that may have reference links appended
    text = re.sub(r'^(\d+)\.\s+(.*?)(?:\s+\(#fnref\d+\))?$', format_footnote, text, flags=re.MULTILINE)
   
    return text

def main():
    """
    Main entry point for the markdown cleanup script.
    """
    # Set up command-line argument parsing
    parser = argparse.ArgumentParser(
        description='Process Markdown file to fix conversion issues from DOCX to Markdown conversion'
    )
    parser.add_argument('input_file', 
                       help='Input Markdown file that needs cleanup')
    parser.add_argument('-o', '--output', 
                       help='Output Markdown file (default: input_file_fixed.md)')
   
    # Parse command-line arguments
    args = parser.parse_args()
   
    # Generate default output filename if none specified
    # Takes input filename and adds '_fixed' before the .md extension
    if not args.output:
        output_file = args.input_file.rsplit('.', 1)[0] + '_fixed.md'
    else:
        output_file = args.output
   
    try:
        # Read the input markdown file with UTF-8 encoding
        # UTF-8 encoding is essential for handling international characters
        # and special symbols that might be present in scientific documents
        with open(args.input_file, 'r', encoding='utf-8') as f:
            content = f.read()
       
        # Apply the markdown cleanup processing
        processed_content = process_markdown(content)
       
        # Write the cleaned content to the output file
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(processed_content)
            
        # Provide user feedback on successful processing
        print(f"Successfully processed '{args.input_file}' -> '{output_file}'")
       
    except FileNotFoundError:
        # Handle case where input file doesn't exist
        print(f"Error: File '{args.input_file}' not found")
        sys.exit(1)
    except Exception as e:
        # Handle any other errors during processing
        print(f"Error while processing: {e}")
        sys.exit(1)

if __name__ == '__main__':
    main()