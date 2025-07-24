# Hinweis zur Nutzung des Markdown Formats

Markdown ist eine Auszeichnungssprache, mit der sich Texte klar strukturiert und leicht lesbar formatieren lassen. Dieses Dokument enthält Beispiele für typische Markdown Formatierungen. Um diese nachvollziehen zu können sollten Sie das Dokument in einem passenden Editor öffnen, um sowohl den Rohtext mit den verwendeten Markdown-Symbolen als auch die finale Darstellung zu sehen. So wird ersichtlich, mit welchen Zeichen die Formatierung erfolgt und wie das Ergebnis aussieht.

## Markdown Editoren

Markdown-Dateien (.md) können in nahezu jedem Texteditor bearbeitet werden. Besonders komfortabel sind spezialisierte Editoren, die eine Live-Vorschau bieten. Ein webbasierter Markdown-Editor ist beispielsweise StackEdit (https://stackedit.io/app#). Eine Liste mit weiteren Markdwoneditoren (Online und Desktop) findet sich hier: https://github.com/mundimark/awesome-markdown-editors/tree/master.

Für Programmierende sind auch VS Code oder die JetBrains IDEs (PyCharm, InelliJ, ...) geeignet, die um zusätzliche Funktionen für das Lesen, Bearbeiten und die Vorschau von Markdown Dokumenten erweitert werden können.

Hilfreiche Erläuterungen zur Markdown-Syntax finden Sie auch hier: https://www.markdownguide.org/basic-syntax/.

## Formatierung

### Überschriften 
Überschriften werden duch das Setzen einer Raute (#) markiert. Dabei gilt: Je tiefer die Überschrift in der Hierarchie liegt, desto mehr Rauten werden angelegt. Im fertigen Dokument werden die Überschriften mit einer Raute (#) - sogenannte H1 Überschriften - am größten, die mit zwei Rauten (##) - H2-Überschriften etwas kleiner, die mit drei Rauten (###) - H3-Überschriften - noch etwas kleiner angezeigt usw.
Wichtig: Zwischen Raute(n) und dem Text der Überschrift muss ein Leerzeichen stehen, da sonst keine Überschrift erkannt wird. 

Beispiel:
# Das ist eine H1-Überschrift
## Das ist eine H2-Überschrift
### Das ist eine H3-Überschrift
#### Das ist eine H4-Überschrift


### Kursivierung
Wenn Sie Textstellen kursiv darstellen möchten, setzen Sie vor und nach den entsprechenden Textstellen Unterstriche (`_`).  Es können sowohl einzelne _Wörter_ als auch _mehrere aufeinanderfolgende Wörter_ kursiv gedruckt werden. Generell ist es wichtig, dass zwischen den Unterstrichen und dem zu kursivierenden Text keine Leerzeichen stehen. 
  
Beispiel 1: In diesem Satz ist nur ein Wort _kursiv_ gedruckt.

Beispiel 2: In diesem Satz sind _mehrere Wörter kursiv gedruckt_.

Beispiel 3: Hier funktioniert die _ Kursivierung nicht _ , weil Leerzeichen zwischen Unterstrich und Text stehen.

### Fettdruck
Wenn Sie Textstellen fett gedruckt darstellen möchten, setzen Sie vor und nach den entsprechenden Textstellen doppelte Sternchen (Asteriske) (`**`).  Es können sowohl einzelne **Wörter** als auch **mehrere aufeinanderfolgende Wörter** fett gedruckt werden. Generell ist es wichtig, dass zwischen den Sternchen und dem zu kursivierenden Text keine Leerzeichen stehen. 
  
Beispiel 1: In diesem Satz ist nur ein Wort **fett** gedruckt.

Beispiel 2: In diesem Satz sind **mehrere Wörter fett gedruckt**.

Beispiel 3: Hier funktioniert der ** Fettdruck nicht ** , weil Leerzeichen zwischen Sternchen und Text stehen.


## Links
Zur Verlinkung von Textstellen, setzen sie das zu verlinkende Textelement in eckige Klammern gefolgt vom Ziel des Links in runden Klammern.

Für eine Verlinkung auf eine externe Seite entspricht das Ziel der URL der Seite.

Beispiel: [TU Darmstadt-Seite](https://www.tu-darmstadt.de)

Innerhalb des Textes können Überschriften referenziert werden. Dies geschieht, indem der sogenannte Anker referenziert wird. Der Anker bestejt aus einer Raute (#) und dem Text der Überschrift, wobei alles in Kleinbuchstaben gesetzt und Leerzeichen durch Bindestriche (-) ersetzt werden. Der Anker für die erste Überschrift dieses Textes wäre also #hinweis-zur-nutzung-des-markdown-formats. Der Link auf diesen Anker sieht dann folgendermaßen aus: 

Beispiel: [Dieser Link führt zur ersten Überschrift](#hinweis-zur-nutzung-des-markdown-formats)

Hinweis: Unabhängig, ob es sich um eine H1, H2, H3, ... Überschrift handelt, wird für den Anker eine Raute (#) verwendet.
  
## Fußnoten
Verweise auf Fußnoten werden in Markdwon ebenfalls in eckige Klammern geschrieben. In der Klammer steht ein Dachsymbol/ Zirkumflex (^) gefolgt von der Zahl der Fußnote. Der Inhalt der Fußnote wird erst ganz am Ende (!) des Dokuments definiert. Dabei beginnt die Definition mit demselben Dachsymbol und der Nummer, gefolgt von einem Doppelpunkt und dem Text der Fußnote.

Beispiel:

Dies ist ein Satz mit einer Fußnote[^1].

... Hier folgt der weitere Text des Dokuments ...

[^1]: Hier steht der Inhalt der Fußnote.

## Listen 
Listen in Markdown lassen sich erstellen, indem man eine Textzeile mit einem Stern Symbol (*) beginnt. In numerierten Listen steht stattdessen eine Zahl mit einem Punkt. Wichtig ist hier, dass zwischen Aufzählungszeichen und Text ein Leerzeichen steht. 

Beispiel: 

* Dies ist eine ungeordnete Liste. 
* Sie enthhält
* drei Punkte.

1. Hier steht eine
2. nummerierte Liste
3. mit drei Stichpunkten. 


## Citekeys
Alle Beiträge werden von der Redaktion unter der Nutzung von Pandoc formatiert und gelayoutet. Aus diesem Grund bitten wir Sie, sämtliche Referenzen als Citekeys anzugeben, d. h. alle In-Text-Verweise werden durch entsprechende Citekeys gesetzt. Citekeys können Sie in Ihrem Literaturverwaltungsprogramm manuell vergeben oder automatisiert generieren. Die meisten Literaturverwaltungsprogramme unterstützen die automatisierte Generierung von Citekeys. In Citavi können Sie diese Option beispielsweise freischalten (siehe:https://www1.citavi.com/sub/manual6/de/index.html?bibtex_keys.html). Wenn Sie mit Zotero arbeiten, können Sie die Erweiterung “Better BibTeX” installieren (https://retorque.re/zotero-better-bibtex/). Für jeden Eintrag in Ihrem Literaturverzeichnis werden dann automatisch Citekeys erstellt. Diese Citekeys nutzen Sie dann in Ihrer Einreichung, um Referenzen zu markieren. 

Ein In-Text Verweis mit einem Citekey beginnt grundsätzlich mit einem @. Darüber hinaus gibt es verschiedene Möglichkeiten die Referenz zu gestalten. Dabei gelten die folgenden Regeln:

* Einfache Referenz in Klammern: [@smith2021] führt zu -> (Smith 2021)
* Direkte Erwähnung: @smith2021 führt zu -> Smith (2021)
* Mehrere Quellen: [@doe2023; @smith2022; @smith2021] führt zu -> (Doe 2023, Smith 2021, 2022) 
* Seitenangabe: [@smith2021, 11 f.] führt zu -> (Smith 2021, 11 f.) 
* Seitenangabe mehrseitig: [@smith2021, 11--14] führt zu -> (Smith 2021, 11-14)
* Mehrere Seitenangaben:[@smith2021, 11--14, 102] führt zu -> (Smith 2021, 11-14, 102)
* Seitenangaben bei direkter Erwähnung: @smith2021 [11--14] führt zu -> Smith (2021, 11-14)
* Kombination der Regeln: [vgl. @Zimmermann-2000, 21-22;@Boekaerts-2000, 418--419, 432] führt -> zu (vgl. Zimmermann 2000, 21–22; Boekaerts und Niemivirta 2000, 418–419, 432)

Weiter Hinweise zur Nutzung von Citekeys finden sie hier: https://pandoc.org/chunkedhtml-demo/8.20-citation-syntax.html

## Gender-Zeichen
Bei der Verwendung eines Gender-Sternchens (*) muss ein sogenanntes Escape-Zeichen verwendet werden, damit das Sternchen nicht als Formatierung erkannt wird. Dieses Escape-Zeichen ist hier ein Backslash `\`. Dieser wird im finalen Dokument nicht mehr sichtbar sein.

Beispiel: Wissenschaftler\*innen

