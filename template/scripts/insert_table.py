import csv
import os
import re

def read_markdown_text(file_path):
    """
    Read a markdown text file and return its contents as a list of lines.
    Removes everything before the '# Inhaltsverzeichnis' heading if it exists.
    
    Function cleans up markdown files by removing any preamble
    content that appears before the main table of contents section.

    Args:
        file_path (str): Path to the markdown file to be read

    Returns:
        list: Lines of the markdown file with the hint/preamble section removed

    Raises:
        FileNotFoundError: If the specified file doesn't exist
        IOError: If the file can't be read due to permissions or other I/O issues
    """
    # Check if the file exists before attempting to read it
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File {file_path} not found.")
    
    try:
        # Open the file with UTF-8 encoding to handle international characters
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
        
        # Remove any content before '# Inhaltsverzeichnis' (Table of Contents in German)
        # This regex pattern matches everything from the start of the file up to the first
        # occurrence of '# Inhaltsverzeichnis' and replaces it with just the heading
        hint_pattern = r'^.*?(# Inhaltsverzeichnis)'
        content = ''.join(lines)
        content = re.sub(hint_pattern, r'\1', content, flags=re.DOTALL)
        
        # Return as list of lines while preserving line endings for proper formatting
        return content.splitlines(True)  # Preserve line endings
    except IOError as e:
        print(f"Error reading file {file_path}: {str(e)}")
        raise

def read_markdown_table(file_path):
    """
    Read a markdown table from file and return its contents as a string.
    Removes any empty lines before the actual table content begins.
    
    Function handles markdown files that contain only table data, cleaning up any whitespace or formatting issues that might
    interfere with table processing.

    Args:
        file_path (str): Path to the markdown file containing the table

    Returns:
        str: Cleaned markdown table content as a single string

    Raises:
        FileNotFoundError: If the specified file doesn't exist
    """
    # Verify file existence before processing
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File {file_path} not found.")
    
    # Read all lines from the markdown table file
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    # Remove leading empty lines before the table starts
    # This ensures clean table formatting without unnecessary whitespace
    stripped_lines = []
    found_table_start = False
    for line in lines:
        if not found_table_start:
            # Look for the first non-empty line to mark the start of table content
            if line.strip():
                found_table_start = True
                stripped_lines.append(line)
        else:
            # Once we've found the table start, include all subsequent lines
            stripped_lines.append(line)

    # Return the cleaned table as a single string
    return ''.join(stripped_lines)

def write_markdown_file(file_path, lines):
    """
    Write a list of lines to a markdown file. 

    Args:
        file_path (str): Path where the file will be written
        lines (list): Lines of text to write to the file

    Raises:
        IOError: If the file cannot be written due to permissions or disk space issues
    """
    try:
        # Write all lines to the specified file with UTF-8 encoding
        with open(file_path, 'w', encoding='utf-8') as file:
            file.writelines(lines)
        print(f"Successfully wrote file: {file_path}")
    except IOError as e:
        print(f"Error writing to file {file_path}: {str(e)}")
        raise

def read_csv_file(file_path):
    """
    Read a CSV file and return its contents as a 2D list.
    Cleans each cell from newline characters and tabs.

    Args:
        file_path (str): Path to the CSV file to be read

    Returns:
        list: 2D list representing the CSV content, where each row is a list of cells

    Raises:
        FileNotFoundError: If the specified CSV file doesn't exist
        csv.Error: If there are issues parsing the CSV format
        IOError: If the file can't be read
    """
    # Verify the CSV file exists before attempting to read it
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File {file_path} not found.")
    
    table = []
    try:
        # Open CSV file with proper encoding and newline handling
        with open(file_path, newline='', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                # Clean each cell by removing newlines, carriage returns, and tabs
                # Replace them with spaces and strip whitespace for clean formatting
                cleaned_row = [re.sub(r'[\r\n\t]+', ' ', cell).strip() for cell in row]
                table.append(cleaned_row)
        
        # Warn if the CSV file appears to be empty
        if not table:
            print(f"Warning: CSV file {file_path} is empty")
        return table
    except csv.Error as e:
        print(f"CSV parsing error in {file_path}: {str(e)}")
        raise
    except IOError as e:
        print(f"Error reading file {file_path}: {str(e)}")
        raise

def convert_csv_to_markdown(table):
    """
    Convert a CSV-style 2D list into markdown table format.

    Args:
        table (list): 2D list with table content, where first row is treated as headers

    Returns:
        str: Markdown representation of the table with proper formatting
    """
    # Return empty string if no table data is provided
    if not table:
        return ''
    
    md_table = []
    
    # Create the header row with proper markdown table syntax
    header_row = '| ' + ' | '.join(table[0]) + ' |'
    
    # Create the separator row that defines column alignment in markdown tables
    # This creates a separator with appropriate dashes based on column content length
    separator_row = '|-' + '-|-'.join(['-' * len(col) for col in table[0]]) + '-|'
    
    # Add header and separator to the markdown table
    md_table.append(header_row)
    md_table.append(separator_row)

    # Add all data rows (excluding the header row)
    for row in table[1:]:
        md_table.append('| ' + ' | '.join(row) + ' |')
    
    # Join all rows with newlines to create the complete markdown table
    return '\n'.join(md_table)

def convert_markdown_to_csv(markdown_table, output_file):
    """
    Convert a markdown-formatted table into CSV format and save to a file.

    Args:
        markdown_table (str): Markdown table string with proper formatting
        output_file (str): Output CSV file path where the data will be saved
    """
    # Split the markdown table into individual rows
    rows = markdown_table.strip().split('\n')
    
    # Extract header row by removing pipe characters and splitting on pipes
    header_row = [cell.strip() for cell in rows[0].strip('|').split('|')]
    
    # Extract data rows, skipping the separator row (index 1)
    data_rows = [row.strip('|').split('|') for row in rows[2:]]  # Skip separator

    # Write the converted data to a CSV file
    with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(header_row)
        writer.writerows(data_rows)
    
    print(f"The markdown table has been saved as a CSV file: {output_file}")

def insert_table(lines, table_markdown, heading_no=4):
    """
    Insert a markdown table after a specified top-level heading.

    Args:
        lines (list): Markdown file lines as a list
        table_markdown (str): Formatted markdown table to insert
        heading_no (int): Index of the heading after which the table should be inserted

    Returns:
        list: Modified markdown lines with the table inserted at the correct position

    Raises:
        ValueError: If the specified heading index is not found in the document
    """
    # Find all top-level headings (lines starting with "# ")
    heading_indices = [i for i, line in enumerate(lines) if line.startswith("# ")]
    
    try:
        # Get the line index of the specified heading
        heading_index = heading_indices[heading_no]
    except IndexError:
        # Provide helpful error message if the heading index is out of bounds
        print(f"Text only contains {len(heading_indices)} level 1 headings. Index {heading_no} is out of bounds")
        return lines

    # Create new document structure:
    # 1. Keep everything before the target heading
    new_lines = lines[:heading_index]
    # 2. Insert the table
    new_lines.append(table_markdown)
    # 3. Skip the next 3 lines (previous placeholder table block if any) and add the rest
    new_lines.extend(lines[heading_index + 3:])

    return new_lines

def exctract_heading(lines, heading_no=4):
    """
    Extract a specific top-level heading line.
    
    This function retrieves a specific heading from the document structure.

    Args:
        lines (list): Markdown lines from the document
        heading_no (int): Index of the heading to extract (0-based)

    Returns:
        str: The heading line, or empty string if heading not found
    """
    # Find all top-level headings in the document
    heading_indices = [i for i, line in enumerate(lines) if line.startswith("# ")]
    
    try:
        # Get the line index of the requested heading
        heading_index = heading_indices[heading_no]
    except IndexError:
        # Handle case where the requested heading doesn't exist
        print(f"Text only contains {len(heading_indices)} level 1 headings. Index {heading_no} is out of bounds")
        return ''
    
    # Return the actual heading line
    return lines[heading_index]

def add_latex_landscape_wrapper(table_markdown, heading):
    """
    Wrap a markdown table with LaTeX landscape and formatting commands.
    
    Adds LaTeX commands to rotate tables to landscape orientation
    and adjust font sizes for better readability in the final PDF output.

    Args:
        table_markdown (str): Markdown table content to be wrapped
        heading (str): Heading to include before the table

    Returns:
        str: Markdown string with LaTeX wrapper commands for PDF processing
    """
    new_table = []
    
    # Begin LaTeX landscape environment for wide tables
    new_table.append('```{=latex}\n')
    new_table.append('\\begin{landscape}\n')
    new_table.append('```\n')
    
    # Add the heading for the table section
    new_table.append(heading)
    
    # Set font size to footnotesize for better table fitting
    new_table.append('```{=latex}\n')
    new_table.append('\\footnotesize\n')
    new_table.append('```\n')
    new_table.append('\n')
    
    # Insert the actual table content
    new_table.append(table_markdown)
    new_table.append('\n\n')
    
    # Close LaTeX environment and restore normal font size
    new_table.append('```{=latex}\n')
    new_table.append('\\end{landscape}\n')
    new_table.append('\\normalsize\n')
    new_table.append('```\n')
    new_table.append('\n')

    # Return the complete wrapped table as a single string
    return ''.join(new_table)

def main(markdown_file, table_file):
    """
    Main entry point to process a markdown document and insert a table into it.

    Workflow:
    1. Read the table file (markdown or CSV format)
    2. Convert the table to markdown format (if necessary)
    3. Read the main markdown article content
    4. Extract the target heading where the table should be placed
    5. Add LaTeX formatting around the table for PDF compatibility
    6. Insert the table at the correct position in the document
    7. Write the updated markdown to a new file

    Args:
        markdown_file (str): Path to the input markdown file (main article)
        table_file (str): Path to the table file (CSV or markdown format)
    """
    try:
        table_markdown = ''
        
        # Handle CSV input files
        if table_file.lower().endswith('.csv'):
            print(f"Reading CSV table from {table_file}")
            # Read CSV data and convert to markdown table format
            table = read_csv_file(table_file)
            table_markdown = convert_csv_to_markdown(table)

        # Handle markdown input files
        elif table_file.lower().endswith('.md'):
            print(f"Reading markdown table from {table_file}")
            # Read markdown table directly
            table_markdown = read_markdown_table(table_file)
            
            # Create a CSV backup of the markdown table for data archival
            csv_file = table_file.replace('.md', '_processed.csv')
            print(f"Converting markdown table to CSV: {csv_file}")
            convert_markdown_to_csv(table_markdown, csv_file)

        # Read the main markdown document
        print(f"Reading markdown text file: {markdown_file}")
        lines = read_markdown_text(markdown_file)
        
        # Process the table if content was successfully loaded
        if table_markdown:
            print("Adding LaTeX landscape wrapper to table")
            # Extract the heading where the table will be placed
            heading = exctract_heading(lines)
            # Wrap the table with LaTeX commands for PDF processing
            table_markdown = add_latex_landscape_wrapper(table_markdown, heading)
            
            # Save the processed table for debugging/verification purposes
            with open('table_processed.md', 'w', encoding='utf-8') as f:
                f.write(table_markdown)
            print("Saved processed table to table_processed.md")
            
            # Insert the table into the main document
            print("Inserting table")
            updated_lines = insert_table(lines, table_markdown)
        else:
            print("Warning: No table content to insert")
            updated_lines = lines

        # Generate output filename based on current directory name
        output_file = f"{os.path.basename(os.getcwd())}_intext_replaced.md"
        print(f"Writing output to {output_file}")
        write_markdown_file(output_file, updated_lines)
        print(f"The file has been updated and saved as: {output_file}")

    except Exception as e:
        print(f"Error in main function: {str(e)}")
        raise

if __name__ == "__main__":
    # Command Line Interface (CLI) for using the script from command line
    # This allows the script to be used as a standalone tool in the PDF generation pipeline
    import argparse
    
    # Set up argument parser for command line usage
    parser = argparse.ArgumentParser(description="Insert a table into a markdown document.")
    parser.add_argument("markdown_file", help="Path to the markdown file.")
    parser.add_argument("table_file", help="Path to the table file (markdown or CSV).")
    args = parser.parse_args()

    # Execute main function with command line arguments
    try:
        main(args.markdown_file, args.table_file)
    except Exception as e:
        print(f"Program failed: {str(e)}")
        exit(1)