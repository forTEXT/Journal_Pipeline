# Abstract

Das vorgestellte Lehrkonzept vermittelt Kompetenzen der digitalen Editorik im Rahmen der Hochschullehre. Der technische Schwerpunkt der vorgestellten Lehrveranstaltung liegt dabei auf der Vermittlung von Auszeichnungssprachen. Ziel ist es, den Teilnehmenden zu ermöglichen, ihren Lernprozess in der praktischen Erprobung editorischer Aufgaben mittels digitaler Annotationen teilweise selbst zu regulieren. Dafür werden Schriftstücke aus dem Liebesbriefarchiv transkribiert und kommentiert.

# Inhalt

1. [Einführung](#einführung)

2. [Gesamtablauf](#gesamtablauf)

3. [Sitzungsübersicht](#sitzungsübersicht)

4. [Reflexion](#reflexion)

# 1. Einführung

Ziel der folgenden Darstellung ist nicht, den Inhalt der Veranstaltung vollständig darzubieten und eine unmittelbare Nachnutzung zu ermöglichen, da dies bei 14 Sitzungen den gebotenen Umfang übersteigen würde. Zudem liegen zu wesentlichen Inhalten der Veranstaltung, nämlich zu XML, zum "Dialekt" der Text Encoding Initiative (TEI) und auch zu den im Bereich der digitalen Editorik besonders relevanten TEI-Modulen bereits ausreichend Lehrmaterialien vor [siehe [TEI by Example](https://www.teibyexample.org/), @Burghart-2017 oder @Schoech-2014]. Die Darstellung reflektiert vielmehr die Ansprüche an das Lehrkonzept und bereits vorgenommene Anpassungen. Darüber hinaus zeigt ein Vergleich mit einer ähnlichen Lehrveranstaltung weitere Anpassungsmöglichkeiten an eigene Angebote auf.

Diese Lehrinhalte können dem Bereich der digitalen Textannotation zugeordnet werden [siehe @Rapp-2017, 255]. In der digitalen Editorik haben sich seit den 1980er Jahren die Vorschläge der TEI verbreitet. Sie werden auch in Richtlinien und Vorgaben von Förderinstitutionen [siehe zum Beispiel @DFG-2015] nahegelegt oder gefordert. Die Vorschläge der TEI beziehen sich auf die Auszeichnungssprache XML. Derartige Sprachen können nicht nur Informationen zu Formatierungen vom eigentlichen Text trennen, sondern auch Strukturen wie Abschnitte und Absätze markieren [siehe @DeRose-1990;@Goldfarb-1981; @Goldfarb-2004, 7--10]. Die in XML gegebene Erweiterbarkeit erlaubt zudem Anpassungen, um mit Annotationen regelgeleitet und maschinenlesbar unter anderem linguistisch, literaturwissenschaftlich und editionsphilologisch relevante Textmerkmale und Schreibphänomene auszuzeichnen. Die Annotationsschemata sind zum einen ein Modell des interessierenden Gegenstandes; zum anderen bilden sie die Grundlage für Suchen und Datenanalysen, in welche die annotierten Dokumente einbezogen werden können.

## 1.1 Rahmenbedingungen

Dieser Beitrag stellt ein Konzept für die Vermittlung digitaler Editorik im Rahmen der Hochschullehre vor, das von einem der Autoren, Philipp Hegel, in der Übung *Textauszeichnung* im Masterstudiengang *Literary and Linguistic Computing* an der Technischen Universität Darmstadt angewendet wird und auf Erfahrungen aus Projektberatungen basiert. Das Konzept wurde über mehr als zehn Jahre erprobt und angepasst. Behandelt werden digitalisierte Privatbriefe der 1950er Jahre aus dem [Liebesbriefarchiv](https://liebesbriefarchiv.de/), die in einem Projekt des Dozenten untersucht werden. Dabei liegen Schwerpunkte auf der Transkription und dem Kommentieren der Briefe. Ziel des Lehrkonzepts ist die Vermittlung theoretischer und praktischer Grundkenntnisse des digitalen Editierens und entsprechender Auszeichnungssprachen.

An der Lehrveranstaltung nehmen in der Regel fünf bis fünfzehn Studierende teil und der Arbeitsaufwand entspricht fünf Leistungspunkten. Zur Prüfungsleistung zählen die aktive Teilnahme in Form von Beteiligungen an praktischen Übungen, zwei Präsentationen, die als Zwischenberichte dienen, sowie Projektarbeiten in Form von zehn transkribierten und kommentierten Briefen im XML-Format. Alle Sitzungen finden in der Regel synchron in Präsenz statt. Die Zahl der Sitzungen kann variieren, wobei im Folgenden von 14 Semesterwochen ausgegangen wird und jede Sitzung 90 Minuten umfasst.

## 1.2 Voraussetzungen der Teilnehmenden

Es werden digitale Kompetenzen vorausgesetzt, weshalb sich die Lehrveranstaltung dezidiert an Masterstudierende richtet. Kursteilnehmende verfügen über grundlegende Kenntnisse und Erfahrungen im Programmieren, haben mit X-Technologien, welche im Lehrkonzept eine zentrale Rolle spielen, jedoch zuvor meist wenig Kontakt gehabt.
Zudem wird vorausgesetzt, dass Teilnehmende eigenständig geeignete Lernstrategien anwenden können und mit dem wissenschaftlichen Arbeiten vertraut sind.

Technisch wird außerdem eine Klassenraumlizenz für den [Oxygen XML Editor](https://www.oxygenxml.com/) vorausgesetzt sowie eine dazu passende Hardwareausstattung der Studierenden. Die in der Lehrveranstaltung gemachten technischen Voraussetzungen haben sich bisher nicht als problematisch erwiesen. Es wird versucht, Studierende dazu zu motivieren, etwaige Hindernisse anzusprechen. Sollten Schwierigkeiten benannt oder offenkundig werden, werden Lösungen seitens des Dozenten in Kooperation mit dem Institut und der Hochschule gesucht.
Studierende werden im Rahmen des Kurses auf Unterstützungsangebote wie die Studienberatung und Mentoringprogramme am Institut sowie auf Beratungsstellen an der Universität hingewiesen.

## 1.3 Ausführungen der Lehrveranstaltung

### 1.3.1 Lehrmaterial

Zur Durchführung der Lehrveranstaltung werden verschiedene Materialien bzw. Medien genutzt und benötigt: Präsentationsfolien, der Oxygen XML Editor sowie eine WLAN-Verbindung. Für besondere Fragen werden Bildschirmaufnahmen erstellt. Auf der Lernplattform werden diese ebenso wie die zu lesenden Texte hinterlegt. Die Lehrmaterialien wurden vom Dozenten selbst erstellt und angepasst.

### 1.3.2 Aufgabentypen

Es gibt wöchentliche Aufgaben (s. Spalte *Abgabe/Aufgabe* in der tabellarischen Sitzungsübersicht). In den Sitzungen selbst werden Ratespiele und Gruppenarbeiten durchgeführt. Zudem sind zwei Zwischenberichte vorgesehen, die als eine Art "Hackathon" veranstaltet werden, bei denen Studierende Kodierungsvorschläge diskutieren, Schwierigkeiten bei der Transkription lösen und kommentierungsbedürftige Stellen klären [vgl. zum Hackathon als "temporäres Labor" @Trilcke-2018; und zur Umsetzung in der akademischen Lehre @Mischke-2022].

### 1.3.3 Lehrstrategischer Ansatz

Die Struktur der Übung hängt eng mit dem gewählten lehrstrategischen Ansatz zusammen, der auf Selbstregulation setzt [siehe hierzu zusammenfassend @Landmann-2015, 53]. Der Planung, Beobachtung, Reflexion und Anpassung von Motivationen, Verfahren und Zielsetzungen im Lernprozess durch die Studierenden selbst sind jedoch institutionelle und organisatorische Grenzen gesetzt. Zum einen sind curriculare Lernziele vorgegeben, zum anderen müssen am Ende Noten für vergleichbare Leistungen vergeben werden [vgl. zu diesen Schwierigkeiten @Boekaerts-2000, 418--419, 432; @Goetz-2017, 148]. In selbstreflexiven Phasen können jedoch diese beiden Aspekte als Kriterien der sogenannten "Meisterschaft" und des normativen Vergleichs auch der studentischen Selbstbewertung dienen [vgl. @Zimmermann-2000, 21--22].

Der Ansatz kann als verteiltes Lernen anhand konkreter Beispiele und Vertiefungsfragen mit Ansätzen zu Verschachtelungen und Lerntests beschrieben werden. Verteilt ist das Lernen, weil diskontinuierlich Themen wiederholt werden [vgl. @Moerth-2021, 43]. Insbesondere dienen die Zwischenberichte dazu, Gelerntes auf das Quellenmaterial anzuwenden und die Ergebnisse sowie Problemfelder gemeinsam zu diskutieren. Zur Motivation und Metakognition [vgl. @Goetz-2017, 152] werden Präsentationen als Selbsttest eingesetzt. Der Motivation und Elaboration dient die Illustration durch verschiedene konkrete Beispiele, darunter vor allem die den Studierenden zugeordneten Briefe. Fragen nach Methode, Zweck und Begründung der eigenen Untersuchungen unterstützen die Elaboration [vgl. @Moerth-2021, 45--56]. Verschachtelt ist das Lernen insoweit, als innerhalb von Unterrichtseinheiten Themenwechsel vollzogen werden [vgl. @Moerth-2021, 44].

Präaktional legt der Dozent Lehrinhalte dar, Bewertungskriterien offen und erkundet mit Umfragen die Vorkenntnisse bzw. macht diese bewusst. Aktional erfolgt die Betreuung mit Einladungen zur Sprechstunde und möglichst vielen Fragemöglichkeiten in den Sitzungen. Die Rückmeldungen dienen auch postaktional der Betreuung [vgl. zu den Phasen @Zimmermann-2000, 16; sowie zusammenfassend @Otto-2015, 45--46].

# 2. Gesamtablauf

Inhaltlich lässt sich die Lehrveranstaltung in sechs Blöcke gliedern. Im ersten Block (Sitzungen 1 bis 3) wird ein gemeinsamer Wissensstand zur Editorik, zum Brief, zu Briefeditionen und zu Auszeichnungssprachen erarbeitet. Auf diese Weise werden etwaige Kompetenzunterschiede eruiert und möglichst ausgeglichen, da diese Themen grundlegend für den weiteren Verlauf der Lehrveranstaltung sind.

Daran schließt sich ein Block an, in dem die Studierenden mit verschiedenen Modulen der TEI-Richtlinien anhand von Beispielen vertraut gemacht werden (Sitzungen 4 bis 6). Nach dem Abgabetermin für die ersten Transkriptionen folgen mehrere Sitzungen, in denen die Studierenden ihre bisherigen Ergebnisse und Probleme vorstellen. Je nach Kursgröße kann die Zahl dieser Sitzungen variieren. Im exemplarischen Plan wurden drei Sitzungen vorgesehen (Sitzungen 7 bis 9).

Es folgt eine Sitzung zur Kommentierung (Sitzung 10). Nach dem Abgabetermin für die ersten kommentierten Transkriptionen folgen wieder entsprechend viele Sitzungen für Zwischenberichte (im Plan Sitzungen 11 bis 13). Abgeschlossen wird die Veranstaltung mit einem Ausblick auf die Fertigstellung der digitalen Edition und weiterführende X-Technologien (Sitzung 14). In längeren Semestern kann dieser Ausblick vertieft werden.

Editorische und gattungstheoretische Konzepte (Sitzungen 1 bis 3) werden in den Sitzungen zur digitalen Annotation (Sitzungen 4 bis 6 sowie 10) aufgegriffen und in der praktischen Anwendung auf konkrete Beispiele von den Lernenden selbständig geübt (Sitzungen 7 bis 9 sowie 11 bis 13). Die Anwendung wird mehrfach in der Gruppe diskutiert und Lernende müssen ihre Entscheidungen und Vorgehen wissenschaftlich begründen. Die Anwendung des Gelernten und die Präsentation der Ergebnisse haben die Funktion von Lerntests. Dabei soll verknüpftes Wissen abgerufen werden, während die Lernfortschritte beobachtet und Rückmeldungen gegeben werden können.

# 4. Tabellarische Sitzungsübersicht 


# 3. Sitzungsübersicht

## 3.1 Grundlagen der Editorik (Sitzung 1)

Editorische Konzepte und Operationen sind Studierenden vor der Veranstaltung in der Regel nur oberflächlich oder gar nicht vertraut. In der ersten Sitzung wird daher auf verschiedene Problemstellungen der Editorik eingegangen:

1. *Heuristik* als die Aufgabe, alle relevanten Textzeugen zu identifizieren, ist für die Veranstaltung selbst von untergeordneter Bedeutung. Da Privatbriefe behandelt werden, die dem Liebesbriefarchiv gespendet wurden, liegen bereits Katalogeinträge vor. In einzelnen Fällen ist dennoch eine Prüfung und gegebenenfalls neue Zuordnung notwendig, wenn beispielsweise Briefe unvollständig oder Seiten falsch sortiert sind.

2. Im Zusammenhang mit der *Prüfung der Authentizität* von Textzeugen wird auf das Beispiel von @Valla-1994 und die Konstantinische Schenkung eingegangen sowie auf Möglichkeiten der Materialanalyse hingewiesen. Da in der Veranstaltung mit Digitalisaten gearbeitet wird, spielen diese Möglichkeiten in späteren Einheiten keine Rolle mehr.

3. Die *Quellenbeschreibung* als ein Moment der Erschließung und als Voraussetzung der editorischen Arbeit ist aufgrund der Verwendung von digitalen Reproduktionen eingeschränkt. Metadaten, die sich speziell auf schriftliche Korrespondenzen beziehen, werden jedoch ausführlich thematisiert.

4. Von besonderer Relevanz für die Lehrveranstaltung sind die *Transkription* und die Berücksichtigung der *Textgenese*, verstanden als die Entstehung des Textes auf dem überlieferten Dokument. Diese Schritte bilden einen der beiden Schwerpunkte.

5. *Textkritik*, *Kollation* und *Stemmatologie* sowie die Methoden der *recensio* und *emendatio* werden erklärt. Weil aber Briefe untersucht werden, die unikal überliefert sind, finden diese im weiteren Kursverlauf keine praktische Anwendung.

6. Neben der Transkription stellt der *Kommentar* den zweiten Schwerpunkt dar. Nach einem Vortrag des Lehrenden über Theorie und Praxis des Kommentars wird das Augenmerk auf die Methoden und die benutzten Quellen bei der Erstellung von Einzelstellenkommentaren gelenkt.

7. Abschließend wird die Frage der *medialen Präsentation* angesprochen. Übliche Verfahren zur Transformation und die Möglichkeiten, die der *Author Mode* im Oxygen XML Editor bietet, werden benannt und zum Teil angewandt.

Dieses Wissen wird in Form einer Umfrage zunächst abgefragt und durch begleitende Erläuterungen des Dozenten vermittelt. Dies ist notwendig, weil es im weiteren Verlauf darum geht, diese Strukturen und Phänomene digital zu modellieren und durch Annotationen zu erfassen.

Es kann demotivierend sein, dass die mediale Präsentation der Ergebnisse kein wesentlicher Teil der Übung ist. In der ersten Sitzung betrachten und analysieren die Studierenden jedoch gedruckte und digitale Editionen und vergleichen deren Schichten und Funktionalitäten. In der abschließenden Sitzung wird dann anhand eines Briefes eine exemplarische Umsetzung in HTML mit dem  vorgeführt, um den gesamten Produktionsprozess der Edition nicht aus dem Blick zu verlieren. Für die Vertiefung werden die Teilnehmenden auf @Plachta-2013, @Plachta-2020 sowie @Sahle-2013 hingewiesen.

## 3.2 Gattungstheorie des Briefes (Sitzungen 2 und 3)

In der Lehrveranstaltung wird in der Folge mit einer Sitzung zur Gattung des Briefes an lebensweltliche und wissenschaftliche Kenntnisse der Teilnehmenden zu diesem Thema angeknüpft. Ziel ist, ein Bewusstsein für die Spezifika des Briefes im Hinblick auf Textstrukturen und Textphänomene zu schaffen, das für deren Behandlung in Editionen und Editionsrichtlinien grundlegend ist. In Gruppen wird zunächst an Definitionen und Explikationen gearbeitet. Die Ergebnisse werden mit Lexikonartikeln verglichen. Für die Vertiefung zu diesem Themenfeld werden @Matthews-Schlinzig-2020-a und @Matthews-Schlinzig-2020-b genannt.

Es werden anschließend Aufsätze zur Edition von Briefen behandelt, die jeweils unterschiedliche Aspekte betonen. Konkret werden die editionswissenschaftlichen Ansätze von @Gregolin-1990, @Zeller-2002 und @Strobel-2019 jeweils in Gruppen behandelt und dann gemeinsam im Plenum diskutiert. Auf diese Weise wird das Wissen über Editionen mit dem Wissen über Briefe in Verbindung gebracht. Ausgewählt wurden diese Aufsätze wegen ihrer konträren Positionen. Der Kurs wird in drei Gruppen geteilt. Jede Gruppe konzentriert sich auf einen der Texte, fasst die Argumentation zusammen und erarbeitet mögliche Gegenargumente sowie deren etwaige Entkräftung. Ein Ergebnis kann sein, dass bei Briefen sowohl textuelle als auch materielle und pragmatische Aspekte editorisch zu beachten sind. Es kann diskutiert werden, wo Schwerpunkte zu legen und wie die Aspekte editorisch umzusetzen sind.

## 3.3 Grundlagen der Textauszeichnung (Sitzungen 2 und 4)

Im informatischen Bereich stehen das Erlernen und das Verständnis von Auszeichnungssprachen im Mittelpunkt der Veranstaltung. Deren Grundannahmen und -anliegen werden daher ausführlicher behandelt. Auszeichnungssprachen (*Markup Languages*) wie SGML, HTML und XML werden eingeführt, ihre Entwicklungen und Funktionen erläutert und reflektiert.

Da in der Lehrveranstaltung keine Kenntnisse im Umgang mit XML-Daten vorausgesetzt werden (siehe Abschnitt 1.2), sind zunächst die Grundlagen in diesem Bereich zu vermitteln (Sitzungen 2 und 4). Diese umfassen unter anderem die Konzepte von deskriptivem Markup sowie von Wohlgeformtheit und Validität. Auf dieser Basis können anschließend die Grundlagen von Textauszeichnungen nach den Richtlinien der TEI vorgestellt werden. Diese umfassen unter anderem die Unterteilung der Dokumente in Kopf (`teiHeader`) und Textkörper (`body`), aber auch die Erfassung elementarer Textstrukturen wie Abschnitte (`div`) und Absätze (`p`). Insgesamt werden vor allem aus den folgenden TEI-Modulen Elemente eingeführt und verwendet:

* `core`

* `header`

* `msdescription`

* `namesdate`

* `textstructure`

* `transcr`

Zentraler Referenzpunkt für Studierenden sind neben den zur Verfügung gestellten Folien die  der TEI die auf der entsprechenden Webseite versammelten Lehrmaterialien. Für die praktische Umsetzungen werden den Studierenden in der Übung eine Beispieldatei, ein RELAX-NG-Schema sowie ein Glossar in der verwendeten Lernplattform zur Verfügung gestellt. Obwohl nur die besagten Module im Kurs detailliert behandelt werden, weicht die Schemadatei nur geringfügig von *TEI-All* ab. *TEI-All* dient als Orientierungspunkt, weil in den Briefen zahlreiche Phänomene wie Bilder, Noten, Verse oder Fragmente aus Theaterstücken auftreten. Die Abweichung von *TEI-All* betrifft die Modellierung von Grußformeln (`salute`) in Briefen. Innerhalb der Veranstaltung und des mit ihr verbundenen Projekts werden diese zusätzlich der Klasse `segLike` zugeordnet, sodass sie abweichend vom Standardmodell auch innerhalb von Absätzen (`p`) vorkommen können.

Falls genug Zeit vorhanden ist und innerhalb des Kurses Interesse besteht, wird gezeigt und erklärt, wie Schemadateien aufgebaut sind und mit dem Werkzeug  Änderungen am Schema vorgenommen werden können. Die Schemadatei dient den Studierenden, um die Validität ihrer Dateien zu prüfen. Die Validität ist zudem neben der Wohlgeformtheit ein Bewertungskriterium für die eingereichten Dateien. Die Beispieldatei zeigt in Verbindung mit dem Glossar und dem Schema auf, welche Tiefe der Auszeichnung bei verschiedenen Textphänomenen erwartet wird.

## 3.4 Quellenbeschreibung (Sitzung 5)

Obwohl in der Übung mit Digitalisaten gearbeitet wird, sollen die materiellen Aspekte der Quellenbeschreibung, die in der Gattungs- und Editionstheorie des Briefes angesprochen werden, nicht vollständig ausgeblendet werden. So wird die mediale Form bezeichnet, indem zum Beispiel zwischen Briefen, Post- und Grußkarten, Telegrammen und Feldpost unterschieden wird. Außerdem werden Schriftträger und Beschreibstoffe grob klassifiziert (vor allem im Rückgriff auf den ) sowie die Erscheinung der Schrift, zum Beispiel die Schriftrichtung, mit `@rend`, `@rendition` und CSS erfasst. Zur Handschriftenbeschreibung (`msDesc`) werden Angaben zu Handlungen, Orten und Personen im Zusammenhang mit dem Korrespondenzgeschehen in `correspDesc` ergänzt. Es werden Register für Entitäten erstellt und in Verbindung mit Briefmarken, Vordrucken und Stempeln (`stamp` und `fw`) können diese Informationen Hinweise auf die situativen Umstände und den historischen Kontext geben. Anhänge und Beilagen (`accMat` und `back`) werden verzeichnet, beschrieben und gegebenenfalls transkribiert. Damit wird die pragmatische Dimension des Briefwechsels erschlossen.

## 3.5 Transkriptionen (Sitzungen 6 bis 9)

Bei der wissenschaftlichen Umschrift wird vor allem die textuelle Dimension der Briefe adressiert. Es wird eine Einheit zur deutschen Paläographie des 20. Jahrhunderts angeboten. In dieser Sitzung wird eine Übersicht über die Entwicklung der Schrift anhand von Tafeln gegeben und ein kurzer Brief aus dem Korpus gemeinsam entziffert. Außerdem werden textgenetische Phänomene wie Ersetzungen (`subst`) behandelt.

## 3.6 Kommentierung (Sitzungen 10 bis 13)

In der Übung ist die Kommentierung von Einzelstellen die zweite zentrale Aufgabe. Die Kommentierung erfolgt mit den Elementen `note`, `term` und `gloss`. Das Lemma (`term`) muss nicht identisch mit dem Ausdruck im Text sein. Als Referenzpunkt im Text können bestehende Auszeichnungen, etwa Absätze (`p`), oder ergänzte Elemente wie `seg` genutzt werden. Das Attribut `@corresp` dient der Verknüpfung von Textstelle und Anmerkung. Die Referenz wird in beide Richtungen gesetzt. Auf diese Weise können mehrere Stellen mit einer Anmerkung verknüpft werden. Exemplarisch kann die Auszeichnung wie folgt aussehen:

```=xml
<seg corresp="#note-01" xml:id="seg-01">
  <rs ref="#Mariawald">Mariawald</rs>
</seg>
. . .
<note type="editorial" corresp="#seg-01" xml:id="note-01">
  <term>Mariawald</term>
  <gloss>Anspielung auf das Schweigegelübde in einem Kloster in der Eifel am gleichnamigen Ort. In seiner Autobiographie beschreibt ...</gloss>
</note>
```

Der Kommentierung bedürftige Ausdrücke können sich zum Beispiel auf Objekte, Orte, Personen und Körperschaften, Zitate und Anspielungen, historische Ereignisse und Zustände beziehen. Die Arbeit an diesen umfasst Verweise auf Normdaten für Entitäten, soll sich aber nicht hierauf beschränken. Vielmehr soll ergänzend kommentiert werden, wenn Identifizierungen schwierig oder nicht eindeutig sind. Ist die Identifikation unproblematisch, wird kein Kommentar verfasst und nur Normdaten im Index verzeichnet.

Den Studierenden wird eingangs eine Liste mit Hilfsmitteln, vor allem Hand- und Wörterbücher verschiedener Disziplinen, an die Hand gegeben. In diesem Fall soll jedoch wie überhaupt versucht werden, die verwendeten Informationen mindestens durch zwei möglichst voneinander unabhängige Quellen zu belegen. Fachspezifische Handbücher und Lexika sollen vor allem "Relais" auf dem Weg zu wichtiger Fachliteratur und historischen Belegen sein, die von den Teilnehmenden auszuwerten ist. Die Kommentare sind somit Ergebnisse zum Teil aufwändiger, von den Studierenden selbst zu leistender Forschung. Quellen für die Erläuterung sollten dem historischen und kulturellen Umfeld immer möglichst nah sein. Da die Briefe Privatdokumente sind, können biographische Quellen, beispielsweise Querverweise zwischen den Briefen, aufschlussreich sein. Um Wiederholungen zu vermeiden, kann auf Kommentare in anderen Briefen verwiesen werden (`ref[@target]`).

Die Studierenden werden in den Briefen oft mit der Lebenswelt der Korrespondierenden unmittelbar konfrontiert. Gerade das, was Schreibenden selbstverständlich und vertraut ist, erschwert oft die Kommentierung. Da die Gruppe manchmal sehr heterogen ist, ergeben sich manchmal lange und komplizierte Recherchepfade, aber auch lehrreiche Diskussionen. Während die Einzelstellenkommentare möglichst kurz sein sollen, wurden in einigen Durchführungen der Übung diese Wege zur Erkenntnis exemplarisch in einem Bericht dargestellt. Im hier vorgestellten Konzept kommen diese Recherchen ausschließlich in den Zwischenberichten vor. Neben Korrektheit, Vollständigkeit und Konsistenz ist aber Selbstständigkeit nach wie vor ein Kriterium von hohem Gewicht bei der Bewertung der Kommentare.

In der ersten Sitzung dieses Blocks wird der Brief, der bereits für die paläographische Übung genutzt wurde, kommentiert. Die Teilnehmenden bestimmen zunächst für sich, was kommentiert werden soll. Nach einer Aussprache darüber, recherchieren sie zunächst für sich alleine, bevor die Ergebnisse in der Gruppe vorgestellt und gemeinsam Kommentare verfasst werden. In der letzten Sitzung der Einheit bringen Studierende ihre Rechercheergebnisse zu ausgewählten Fragen zugeloster anderer Teilnehmender ein.

# 4. Reflexion

## 4.1 Rahmenbedingungen und Ausführung der Veranstaltung

1. Aufgetreten sind in der Lehrveranstaltung vormals Schwierigkeiten vor allem beim selbstbestimmten Formulieren einer Forschungsfrage sowie bei der Begrenzung der Fragestellung in Hinblick auf die zur Verfügung stehende Zeit. Es wurden schon im Vorhinein Maßnahmen getroffen, um auf diese erwarteten Schwierigkeiten zu reagieren. Um Fehlplanungen vorzubeugen, wurden eingangs jeweils eine Projektplanung mit Zeitgerüst von den Studierenden entwickelt sowie mehrere Zwischenberichte mit Rückmeldungen eingeplant. Um Blockaden bei der Themenfindung vorzubeugen, wurde vom Dozenten ein Repertoire von Materialien und Aufgaben angelegt, auf das bei Bedarf und nach individuellem Interesse der Studierenden zurückgegriffen werden konnte.

2. Im Laufe der Jahre wurde mit einer stärkeren Normierung von Material und Aufgaben auf die genannten Probleme reagiert. Ursprünglich wurde in der Übung, die das selbstregulierte Lernen fördern soll und dieses auch voraussetzt, den Teilnehmenden selbst überlassen, eine für sie interessante Forschungsfrage zu formulieren. Der Gegenstand musste im Bereich der digitalen Annotationen liegen, aber nicht notwendigerweise in dem der digitalen Editorik. Dies führte zu einem hohen Betreuungsaufwand, da die Leistungen trotz heterogener Profile der Studierenden in Bezug auf editorische, informatische und sprachliche Kompetenzen vergleichbar sein müssen (siehe Abschnitt 1.3.3). Die beiden genannten Strategien, also der Entwurf eines Zeitplans und die Bereithaltung von Materialien, wurden auch beibehalten, nachdem das Lehrkonzept angepasst wurde. Die Quellen aus dem Liebesbriefarchiv waren zunächst nur eine solche Option aus dem Repertoire, wurden im Sinne der Vergleichbarkeit aber später zu dem gemeinsam bearbeiteten Material. Diese gemeinsame Datengrundlage hat dabei auch zu mehr Austausch zwischen den Teilnehmenden geführt sowie gegenseitigen Hilfestellungen ermöglicht. In der Lernplattform wird zur Unterstützung dieses Austausches ein Forum genutzt. Die Entwicklung einer eigenen Forschungsfrage wurde zwischenzeitlich auf einen schriftlichen Bericht zu einer für besonders interessant gehaltenen Frage der Kommentierung reduziert. Mittlerweile wird nur noch bei den zwei mündlichen Präsentationen berichtet. Entwarfen die Studierenden zuvor ihre eigenen Projekte, so arbeiten sie nun gemeinsam an einem Projekt mit. Der Anteil selbstregulierten Lernens ist damit eingeschränkt gegenüber dem früheren Vorgehen und auch gegenüber anderen Konzepten, wie sie @Walsh-2023 im Hinblick auf heterogene Lerngruppen beschreibt.

3. Das Fehlen einer praktischen Einheit zur Erstellung einer Webpräsentation, wie sie im holistischen Ansatz von @Rehbein-2012 und in vergleichbaren Lehrveranstaltungen (siehe Abschnitt 4.3) beinhaltet ist, kann ein Nachteil für die studentische Motivation sein, da nicht der gesamte Produktionsprozess einer digitalen Edition durchlaufen wird. Umgekehrt bewirkt diese Reduktion eine Konzentration der Lehrinhalte und -ziele auf andere Aspekte der editorischen Arbeit und schließt auch nicht aus, dass der gesamte Prozess bis zur fertigen Edition samt verschiedener dazu geeigneter Technologien angesprochen wird. Um den Prozess vollständig dazustellen und den erfolgreichen Abschluss der Arbeit vor Augen zu führen, spielt nunmehr der Dozent die Daten in eine eher minimalistisch gehaltene Oberfläche ein, um das Ergebnis in der Abschlusssitzung zu zeigen (siehe Abschnitt 3.1).

4. Es blieb trotz der Änderungen am Gesamtkonzept ein Ziel, selbstreguliertes Lernen zu fördern. Dabei sollte zum einen ein hoher Grad an Transparenz für die Benotung gegeben sein, zum anderen sollten die Studierenden durch den computer- und editionsphilologischen Umgang mit historischen Archivmaterialien in ein Arbeitsfeld eingeführt werden, mit dem viele zuvor nur am Rande oder gar nicht in Kontakt gekommen sind. Auf selbstreguliertes Lernen wird damit nicht vollkommen verzichtet, zumal die Studierenden die Zeit für die Transkription und Kommentierung weitgehend selbst einschätzen müssen. Sie arbeiten dabei zwischen den Sitzungen und nach Ende der Vorlesungszeit unter Selbstkontrolle und -regulation, das heißt weitgehend ohne Kontakt mit dem Lehrenden [siehe @Zimmermann-2000, 30--31]. Ein eigener Gestaltungsraum zur Umsetzung des Vorhabens wird gewahrt, indem für die Zwischenberichte nur Mindestzahlen an Briefen festgelegt werden. Auch können die Studierenden zu diesen Zeitpunkten die Materialien unterschiedlich tief erschlossen haben. Eigene Nachforschungen sind zudem für die Kommentierung unumgänglich. Bei den Transkriptionen treten ferner oftmals neue Phänomene auf, die modelliert und ausgezeichnet werden müssen. Mit den Zwischenberichten haben die Teilnehmenden die Möglichkeit, Schwierigkeiten anzusprechen und gemeinsam mit dem Dozenten und der Gruppe Lösungen zu finden. Es wurden auch in jedem Kurs Einheiten vorgesehen, in denen sich je zwei Studierende gegenseitig austauschen und ihre Arbeiten beurteilen (siehe Abschnitt 3.6).

## 4.2 Studierende

Da die Lernenden insbesondere im Bereich der Editorik sowie im Umgang mit XML heterogene Vorkenntnisse aufweisen, werden in der Veranstaltung entsprechende Kenntnisse mittlerweile nicht mehr vorausgesetzt und bestimmte Inhalte wie XSLT und XQuery zurückgestellt. Dafür sollte der Umgang mit historischen Schriftdokumenten als Bestandteil der Ausbildung beibehalten werden, weshalb die Einheit zur Paläographie hinzugefügt wurde. Dabei wurde die frühzeitige gemeinsame Transkription eines Briefes als eine notwendige Ergänzung gesehen. Die Heterogenität der Kompetenzprofile wird darüber hinaus durch häufige Gruppenarbeiten in den Sitzungen vor Ort kompensiert.

Die curricularen Rahmenbedingungen standen nicht im Zentrum dieses Beitrags. Dennoch ist der Zusammenhang vermutlich nicht zweifelhaft. Selbst bei Veranstaltungen in vergleichbaren Studiengängen stellen sich rasch Unterschiede heraus. In Studiengängen der Digitalen Geisteswissenschaften können oftmals Kenntnisse zu Datenmodellierung und -verarbeitung angenommen werden. Der Bedarf, diese im Hinblick auf digitale Editionen grundlegend zu vermitteln, besteht in der Fachgemeinschaft indes weiterhin. Dies zeigt das Interesse an Formaten wie einem Workshop [@Hegel-2023], der eine Abwandlung des vorhandenen Kurskonzeptes darstellt und mit Einheiten aus ähnlichen Lehrveranstaltungen kombiniert wurde.

Aufgrund der verschiedenen Anforderungen an derartige Übungen, vor allem aufgrund der Vermittlung nicht nur editorischer, sondern auch computerphilologischer Kompetenzen (siehe Abschnitt 1) werden vergleichbare Veranstaltungen andernorts auf zwei Semester verteilt. Mit Blick auf die digitalen Kompetenzen erscheint es eine Überlegung wert, ob editorische Kenntnisse in philologischen und ähnlichen Studiengängen gleich mit digitalen Methoden verbunden werden können.

Ähnlich wie die praktische Editorik theoretische Erkenntnisse über den edierten Gegenstand voraussetzt und ermöglicht, kann der Unterricht idealiter in der Textkodierung eine Reflexion der digitalen Praktiken von Datenstrukturierung und -verarbeitung ermöglichen [vgl. @McCarty-2005; @Burnard-2018, 108--109, 112--114; sowie @Sahle-2015]. Dies betrifft nicht nur die Frage, wie der Gegenstand digital adäquat modelliert kann, sondern auch die Frage, wie er digital präsentiert und bereitgestellt werden soll. Ein solcher Unterricht steht vor der Aufgabe, sowohl den Gegenstand der Edition zu überdenken als auch die medialen Spezifika der digitalen Verarbeitung. Man kann dies positiv wenden: Der Unterricht ermöglicht idealerweise eine tiefere Einsicht in das behandelte Objekt und in die Methode seiner Behandlung, indem Strategien zur Datenmodellierung und -verarbeitung gefunden werden, die dem Gegenstand und der Fragestellung angemessen sind [vgl. @Behrmann-1991, v.a. 8 und 11; sowie @Mahony-2012, 223--224].

### 4.3 Alternativen

In vergleichbaren Lehrkontexten können die einzelnen Schritte anders gewichtet sein. Wenn der Fokus auf dem Erproben von standardisierten Workflows und Tools liegt, spielen die editorischen Grundlagen eine indirektere Rolle. In Bezug auf die Punkte 1 bis 5 aus Abschnitt 3.1 werden dann bspw. Problemfelder nur angesprochen und auf vertiefende Literatur sowie Recherchemittel wie das  zum Selbststudium hingewiesen. In anderen Veranstaltungen wird auf die *Kommentierung* verzichtet, während sich ein ganzer Block dem Themenfeld *Mediale Präsentation* widmet. Im Rahmen des Blocks *Transkription* (s. Abschnitt 3.5) wird in vergleichbaren Veranstaltungen üblicherweise auch das einschlägige TEI-Kapitel zum kritischen Apparat (`textcrit`) mit den verschiedenen Ansätzen der lokalen Referenz, der doppelten Endpunktmarkierung und der parallelen Segmentierung behandelt. Es wird aber im hier vorgestellten Lehrkonzept bewusst ausgespart, da es aufgrund der Quellenlage eine weniger wichtige Rolle spielt.

Je nach Studienmöglichkeiten können die fachlichen Hintergründe der Studierenden variieren, sodass sich auch Inter- und Transdisziplinarität unter Umständen als weitere Lernziele anbieten. Methodische Varianz kann durch den zeitlichen Rahmen oder durch die Anbindung an Forschungsvorhaben begründet sein, aber auch im Hinblick auf die vorausgesetzten Kompetenzen erfolgen. Welche Möglichkeiten hier offen stehen, sollen folgende Hinweise zu einem vergleichbaren Kurs andeuten, der auf einer Übung zu X-Technologien aufbaut und auf eine Veranstaltung zu Webtechnologien vorbereitet:

Statt Briefe manuell zu entziffern, erschließen in diesem Kurs zunächst alle Teilnehmenden je einen handgeschriebenen Brief und ein Typoskript mit , um praktische Erfahrung mit einem gängigen OCR/HTR-Werkzeug zu erlangen. In einer anschließenden Gruppendiskussion werden dann typische Problemfälle gemeinsam herausgearbeitet. Zusätzlich können Studierende vorhandene XSLT-Kenntnisse vertiefen, indem sie ein eigenes Skript zur Transformation des eScriptorium-Outputs in valides TEI entwickeln.

In einem zweiten Schritt entwickeln die Teilnehmenden unter Hilfestellung ein XSLT-Skript, das Personen und Orte extrahiert. Das so generierte Personenregister wird dann mit  um Normdaten ([GND](https://gnd.network/)-IDs) angereichert. Umgekehrt erfolgt die Anreicherung des Ortsregister durch manuelle Recherche in , sodass die Teilnehmenden beide Wege kennenlernen. Des weiteren erfassen die Studierenden Normdaten als CMIF [@Dumont-2020] im Metadatenblock der TEI-Dokumente, was eine Validierung und Vorschau über den im Briefkontext weit verbreiteten Webservice  [@Dumont-2016] ermöglicht.

Um die Methodenvielfalt in den Digitalen Geisteswissenschaften aufzuzeigen, enthält der Vergleichskurs auch eine kleine Einheit mit Einblicken in Nachbardisziplinen wie dem *Natural Language Processing*. Diese beginnt mit einer freien Exploration der Briefinhalte mit den , gefolgt von einem gemeinsamen Erkenntnisaustausch. Darüber hinaus hat die Kursleitung Batch- bzw. Shellskripte vorbereitet, die XSLTs mit dem  (@Schmid-1995) kombinieren, um die TEI-Texte in eine lemmatisierte Version zu transformieren. Auf diese Weise lernen die Teilnehmenden alternative Kodierungs- und Analysemöglichkeiten kennen und können deren Vor- und Nachteile explorieren und diskutieren.

Abschließend bereitet eine Gruppe von Studierenden das Personenregister zu einer HTML-Ansicht auf, während eine andere eine Briefeinzelansicht mit XSLT generiert, sodass sie praxisnahe Einblicke in alle Abschnitte eines digitalen Editionsprozesses erfahren.

Alle diese real praktizierten Lehreinheiten sollen zeigen, dass das vorgestellte Lehrkonzept in der Regel nicht *in toto* übertragen werden kann. Die Modularität sowohl der einzelnen Werkzeuge als auch der TEI-Richtlinien erleichtern allerdings die Übernahme einzelner Bestandteile aus diesem Konzept oder dem eingangs genannten frei zugänglichen Lehrmaterial. Die Auswahl der Module hängt von verschiedenen Faktoren ab: a) von den Kompetenzprofilen der Teilnehmenden, b) der Einbindung in Curricula mit ihren jeweiligen Voraussetzungen, Lernzielen und Zeitgerüsten, c) der Anbindung an Forschungsprojekte sowie d) den individuellen wie institutionellen technischen Voraussetzungen. Ein weiterer, aber entscheidender Faktor wurde dabei noch nicht genannt: e) die Kompetenzprofile der Lehrenden.
