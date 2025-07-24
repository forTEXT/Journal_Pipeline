import csv
import os

def read_markdown_file(file_path):
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Die Datei {file_path} wurde nicht gefunden.")
    
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.readlines()

def write_markdown_file(file_path, lines):
    with open(file_path, 'w', encoding='utf-8') as file:
        file.writelines(lines)

def read_csv_file(file_path):
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Die Datei {file_path} wurde nicht gefunden.")
    
    table = []
    with open(file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            cleaned_row = [cell.replace('\n', ' ').replace('\r', '') for cell in row] # test
            table.append(cleaned_row)
            # table.append(row)
    return table

def convert_table_to_markdown(table):
    if not table:
        return ''
    md_table = []
    
    # Header row
    header_row = '| ' + ' | '.join(table[0]) + ' |'
    separator_row = '|-' + '-|-'.join(['-' * len(col) for col in table[0]]) + '-|'
    
    md_table.append(header_row)
    md_table.append(separator_row)
    
    # Data rows
    for row in table[1:]:
        md_table.append('| ' + ' | '.join(row) + ' |')
    
    return '\n'.join(md_table)

def insert_table_before_third_heading(lines, table_markdown):
    headings = [i for i, line in enumerate(lines) if line.startswith('# ')]
    
    if len(headings) < 3:
        raise ValueError("Es gibt weniger als drei Level-1-Überschriften.")
    
    third_heading_index = headings[2]
    
    new_lines = lines[:third_heading_index]

    # Neue Zeilen für LaTeX-Befehle hinzufügen
    new_lines.append('```{=latex}\n')
    new_lines.append('\\begin{landscape}\n')
    new_lines.append('```\n')
    new_lines.append('\n')
    
    # Tabelle hinzufügen
    new_lines.append(table_markdown)
    
    # LaTeX-Befehl für Querformat beenden
    new_lines.append('\n\n')
    new_lines.append('```{=latex}\n')
    new_lines.append('\\end{landscape}\n')
    new_lines.append('```\n')
    new_lines.append('\n')
    
    # Rest des Dokuments wiederherstellen
    new_lines.extend(lines[third_heading_index:])
    
    return new_lines

def main(markdown_file, table_file):
    
    # Überprüfe, ob die Tabelle vorhanden ist und konvertiere sie in Markdown
    table_markdown = ''
    if table_file.lower().endswith('.csv'):
        table = read_csv_file(table_file)
        table_markdown = convert_table_to_markdown(table)

        # Speichern von table.md
        table_md_file = "table.md"
        with open(table_md_file, 'w', encoding='utf-8') as file:
            file.write(table_markdown)
        print(f"Die Tabelle wurde als Markdown-Datei gespeichert: {table_md_file}")

    elif table_file.lower().endswith('.md'):
        with open(table_file, 'r', encoding='utf-8') as file:
            table_markdown = file.read()
    else:
        raise ValueError("Unterstützte Dateiformate für die Tabelle sind .csv und .md")
    
    # Lese die Markdown-Datei
    lines = read_markdown_file(markdown_file)
    
    # Füge die Tabelle hinzu, wenn vorhanden
    if table_markdown:
        updated_lines = insert_table_before_third_heading(lines, table_markdown)
    else:
        updated_lines = lines
    
    # Generiere den Ausgabedateinamen
    output_file = f"{os.path.basename(os.getcwd())}_intext_replaced.md"
    
    write_markdown_file(output_file, updated_lines)
    print(f"Die Datei wurde aktualisiert und gespeichert als: {output_file}")

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Füge eine Tabelle in ein Markdown-Dokument ein.")
    parser.add_argument("markdown_file", help="Pfad zur Markdown-Datei.")
    parser.add_argument("table_file", help="Pfad zur Tabelle (Markdown oder CSV).")
    args = parser.parse_args()
    
    main(args.markdown_file, args.table_file)
