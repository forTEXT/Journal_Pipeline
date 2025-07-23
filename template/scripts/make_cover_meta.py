import sys
import yaml
import re
import os
import difflib
from PyPDF2 import PdfReader

def sanitize_filename(name):
    """
    Converts a string into a safe file name by replacing special characters
    with underscores and reducing consecutive underscores.
    """
    name = re.sub(r'[^\w\-_]', '_', name)  # Replace illegal characters
    name = re.sub(r'_{2,}', '_', name)     # Avoid double underscores
    return name

def find_most_similar_pdf(appendix_title, pdf_dir):
    """
    Finds the most similar PDF file in the given directory based on the appendix title.
    Uses fuzzy matching via difflib.
    """
    if not os.path.exists(pdf_dir):
        return None

    # List all PDF files in the directory
    pdf_files = [f for f in os.listdir(pdf_dir) if f.lower().endswith(".pdf")]
    if not pdf_files:
        return None

    # Find the closest match to the appendix title
    matches = difflib.get_close_matches(appendix_title, pdf_files, n=1, cutoff=0.1)
    if matches:
        return os.path.join(pdf_dir, matches[0])  # Return full path to matched file
    return None

def is_pdf_landscape(pdf_path):
    """
    Determines whether a PDF is in landscape orientation.
    Checks the width and height of the first page.
    """
    try:
        reader = PdfReader(pdf_path)
        page = reader.pages[0]
        width = float(page.mediabox.width)
        height = float(page.mediabox.height)
        return width > height  # Landscape if width > height
    except Exception as e:
        print(f"Error reading PDF file '{pdf_path}': {e}")
        return False  # Default to portrait if an error occurs

def extract_appendices(metadata_file):
    """
    Extracts appendix information from a metadata file (.md with YAML front matter)
    and creates a separate metadata file for each appendix (used to generate cover pages).
    """
    # Read the metadata file
    with open(metadata_file, "r", encoding="utf-8") as file:
        content = file.read().split("---")  # YAML blocks are separated by '---'
        if len(content) < 3:
            print("Error: No valid metadata found.")
            sys.exit(1)

        metadata = yaml.safe_load(content[1])  # Parse YAML block

    # Extract general article metadata
    article_title = metadata.get("title", "Unknown Article")
    article_doi = metadata.get("article", {}).get("doi", "")
    appendices = metadata.get("appendices", [])
    issue = metadata.get("volume")
    volume = metadata.get("issue")
    issuetitle = metadata.get("issuetitle")

    # Set base directory and appendix PDF folder
    base_dir = os.path.dirname(os.path.abspath(metadata_file))
    appendix_dir = os.path.join(base_dir, "Anhänge")

    # If no appendices are defined, stop here
    if not appendices:
        print("No appendices found.")
        sys.exit(0)

    # Process each appendix entry
    for appendix in appendices:
        title = appendix.get("title", "Unknown Title")
        author = appendix.get("author", "Unknown Author")
        date = appendix.get("date", "Unknown Date")

        # Create a safe file name for output
        safe_title = sanitize_filename(title)
        appendix_meta_file = f"{safe_title}_appendix_meta.md"

        # Try to find matching PDF and check if it's landscape
        pdf_path = find_most_similar_pdf(safe_title, appendix_dir)
        landscape = is_pdf_landscape(pdf_path) if pdf_path else False

        # Write a separate metadata file for this appendix
        with open(appendix_meta_file, "w", encoding="utf-8") as out_file:
            out_file.write("---\n")
            out_file.write(f"article_title: \"{article_title}\"\n")
            out_file.write(f"article_doi: \"{article_doi}\"\n")
            out_file.write(f"appendix_title: \"{title}\"\n")
            out_file.write(f"author: \"{author}\"\n")
            out_file.write(f"date: \"{date}\"\n")
            out_file.write(f"issue: \"{issue}\"\n")
            out_file.write(f"volume: \"{volume}\"\n")
            out_file.write(f"issuetitle: \"{issuetitle}\"\n")
            out_file.write(f"landscape: {str(landscape).lower()}\n")  # Write true/false in lowercase
            out_file.write("---\n")

        print(f"Metadata file '{appendix_meta_file}' created.")

# Main program entry point
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Error: No input file specified.")
        sys.exit(1)

    # Start the appendix extraction
    extract_appendices(sys.argv[1])
