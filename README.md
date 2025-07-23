# Journal_Pipeline
** Copy unser Artikelpipeline für die ULB **

# forTEXT Zeitschrift

Privates Repository, indem externe Einreichungen zu PDF-XML-Dateien umgewandelt werden.

**Kontext**: Autor\*innen nutzen für die Einreichung von Beiträgen die Submission-Guidelines und -Templates auf journal.fortext.org. Diese geben streng Formate der Einreichung sowie inhaltlichen Aufbau der Einreichungen vor. 
forTEXT führt die Konvertierung und somit Erstellung finaler Artikeldateien in XML-JATS- und PDF-Format selbstständig durch. Dafür wird die Pipeline im Ordner "template" genutzt.
forTEXT übernimmt eine sogenannte "formale Prüfung" die im Rahmen der Ausführung dieser Pipeline durchgeführt wird: Sollten Dateien unvollständig oder im falschen Format vorhanden sein, gibt die Pipeline Fehlermeldungen aus. Im schlimmsten Fall ist eine Generierung der XML- und PDF-Versionen nicht möglich. Die Fehlermeldungen werden im Rahmen der formalen Prüfung an die Autor\*innen weitergeleitet und Fehler müssen von diesen korrigiert werden.

## Directory strcuture
- **archive**: contains past article versions
- **submission**: contains currently edited article versions
- **template**: contains all templates, codes etc. of the article pipeline
    - content:
        - **shell skripts**
            - mkarticles.sh: Main script to be executed in terminal to generate output XML JATS and PDF in specified directory path(s)
            - mkappendix.sh: automatically executed when appendices are found
            - md_to_docx.sh: convert markdown to docx
            - WORK IN PROGRESS: mkarticles_docx.sh > script for docx-pipeline
        - **files**
            - articles.txt: specify directory path(s) for article pipepline
            - fortext-hefte.yaml

        - **directories** 
            - data: contains files for formating 
                - csl: contains citation styles
                - default: contains font styles
                - filter: contains different filters for formating 
                - logo: cotnains fortext logo 
                - templates: contains templates for article files (latex, jats, html)
            - skripts: contains additional files used in the pipeline
                - fix_markdown.py
                - format_xml.py: used in mkarticles to adjust xml-verison
                - insert_table.py: contains code that inserts the csv/md file of the table into the markdown file to be converted to pdf/jats
                - make_cover_meta.py: used in mkappendices.sh to gather meta information for apemndix header




## Execute Article Pipeline

1. Put folder according to submission guidelines 
    Note: folder needs to contain the following files: author_meta.yaml, text.md, table.csv/table.md,bibliogrphy.bib/.json/.bibtex

2. Navigate to template/ 

3. Specify the folder path in template/articles.txt

3. Run ./mkarticles in terminal/command line

