# Bilder Verwaltung
Dieses Repository beinhaltet die folgenden 4 Programme zur vereinfachten Verwaltung deiner Bilder:
1. **Bilder_Namen_Vereineitlichen**
	Vereinheitlicht die Namen von Bildern die mit verschiedenen Kameras aufgenommen wurden.
	Ermöglicht das chronologische präsentieren und sortieren nach Namen.
1. **Aufnahmedatum_Anpassen**
	Verrechnet einen Offset mit dem Aufnahmedatum eines Bildes.
	Ermöglicht Korrekturen wenn Bilder mit verschiedenen Zeitzonen Einstellungen aufgenommen wurden.
1. **Name_Als_Aufnahmedatum**
	Setzt den Namen eines Bildes als Aufnahmedatum.
	Ermöglicht es fehlende Aufnahmedaten (zum Beispiel bei WhatsApp Bildern) zu ergänzen.
1. **Dateigroesse_Reduzieren**
	Reduziert die Dateigröße von Bildern.
	Ermöglicht das platzsparende speichern von Bildern die man sowiso niemals in Leinwandgröße ausdrucken will.

***
## Download der Programme:
Du kannst dir alle Programme kostenlos auf meiner Website runterladen: [Bilder Verwaltung] (https://...)
Den Quellcode findest du auf GitHub: [Bilder Verwaltung] (https://...)

***
## Verwendung der Programme:
1. Programme runterladen.
1. .zip Datei entpacken.
1. Zu bearbeitende Dateien in den input Ordner kopieren.
1. Programm ausführen (siehe - Ausführung der Programme - Abschnitt für mehr Details).
1. Ergebnisse prüfen.

***
## Ausführung der Programme:
1. **Bilder_Namen_Vereineitlichen**
Die Anwendung des Programmes ist sehr einfach und in [diesem Video] (https://...) erklärt.
![Bilder Namen Vereinheitlichen](https://trustmeimanengineer.de/wp-content/uploads/2018/05/UnifyPictureNames.png)
	1.1. Führe die Bilder_Namen_Vereineitlichen.exe Datei durch doppelklick aus.
	1.1. Es öffnet sich ein Konsolen Fenster in dem du gefragt wirst, in welchem Pfad sich die Bilder befinden deren Namen du vereinheitlichen möchtest.
	Gib diesen relativ zum Ausführort des Programmes an oder drücke einfach Enter um den Standard Pfad ("input" Ordner) zu nutzen.
	1.1. Als nächstes wirst du nach dem gewünschten Ausgabeordner gefragt.
	Gib auch diesen relativ zum Ausführort des Programmes ein oder drücke Enter um den Standard Pfad ("output" Ordner) zu nutzen.	
1. **Aufnahmedatum_Anpassen**
Die Anwendung des Programmes ist sehr einfach und in [diesem Video] (https://...) erklärt.
![Bilder Namen Vereinheitlichen](https://trustmeimanengineer.de/wp-content/uploads/2018/05/UnifyPictureNames.png)
	1.1. Führe die Aufnahmedatum_Anpassen.exe Datei durch doppelklick aus.
	1.1. Es öffnet sich ein Konsolen Fenster in dem du gefragt wirst, in welchem Pfad sich die Bilder befinden deren Namen du vereinheitlichen möchtest.
	Gib diesen relativ zum Ausführort des Programmes an oder drücke einfach Enter um den Standard Pfad ("input" Ordner) zu nutzen.
	1.1. Als nächstes wirst du nach dem gewünschten Ausgabeordner gefragt.
	Gib auch diesen relativ zum Ausführort des Programmes ein oder drücke Enter um den Standard Pfad ("output" Ordner) zu nutzen.
	1.1. Anschließend kannst du den gewünschten Zeit Offset als Ganzzahl in Sekunden angeben. Um ein früheres Aufnahmedatum einzustellen kannst du einfach negative Zahlen angeben. 
1. **Name_Als_Aufnahmedatum**
Die Anwendung des Programmes ist sehr einfach und in [diesem Video] (https://...) erklärt.
![Bilder Namen Vereinheitlichen](https://trustmeimanengineer.de/wp-content/uploads/2018/05/UnifyPictureNames.png)
	1.1. Führe die Name_Als_Aufnahmedatum.exe Datei durch doppelklick aus.
	1.1. Es öffnet sich ein Konsolen Fenster in dem du gefragt wirst, in welchem Pfad sich die Bilder befinden deren Namen du vereinheitlichen möchtest.
	Gib diesen relativ zum Ausführort des Programmes an oder drücke einfach Enter um den Standard Pfad ("input" Ordner) zu nutzen.
	1.1. Als nächstes wirst du nach dem gewünschten Ausgabeordner gefragt.
	Gib auch diesen relativ zum Ausführort des Programmes ein oder drücke Enter um den Standard Pfad ("output" Ordner) zu nutzen.
1. **Dateigroesse_Reduzieren**
Die Anwendung des Programmes ist sehr einfach und in [diesem Video] (https://...) erklärt.
![Bilder Namen Vereinheitlichen](https://trustmeimanengineer.de/wp-content/uploads/2018/05/UnifyPictureNames.png)
	1.1. Führe die Dateigroesse_Reduzieren.exe Datei durch doppelklick aus.
	1.1. Es öffnet sich ein Konsolen Fenster in dem du gefragt wirst, in welchem Pfad sich die Bilder befinden deren Namen du vereinheitlichen möchtest.
	Gib diesen relativ zum Ausführort des Programmes an oder drücke einfach Enter um den Standard Pfad ("input" Ordner) zu nutzen.
	1.1. Als nächstes wirst du nach dem gewünschten Ausgabeordner gefragt.
	Gib auch diesen relativ zum Ausführort des Programmes ein oder drücke Enter um den Standard Pfad ("output" Ordner) zu nutzen.
	1.1. Anschließend kannst du die gewünschte Qualität der Bilder als Wert zwischen 1 (gering) und 95 (hoch) angeben.
	Je geringer die Qualität gewählt ist, desto geringer wird auch der benötigte Speicherplatz für die Bilder werden. Als Standard Wert wird 75 verwendet.

***
## Funktion der Programme:
1. **Bilder_Namen_Vereineitlichen**
Das Programm erstellt zuerst eine Liste aller Dateien in dem ausgewählten input Ordner und allen Unterordnern.
Bearbeitet werden nur .jpg, .jpeg und .png Dateien, alle anderen werden ohne Anpassungen kopiert.
Zuerst werden die Metadaten der Datei ausgelesen und es wird versucht das Aufnahmedatum des Bildes zu ermitteln.
Wenn das Aufnahmedatum vorhanden ist, wird die Datei kopiert und mit dem Aufnahmedatum als Dateinamen im Format YYYYMMDD_hhmmss gespeichert.
Wenn kein Aufnahmedatum vorhanden ist, aber der Dateiname "WA" (WhatsApp) enthält, wird das führende "IMG-" im Dateinamen gelöscht.
Alle Dateien werden im angegebenen Output Ordner mit einem Eindeutigen Namen gespeichert.
Wenn zwei Bilder den selben Namen erhalten würden, wird keine Datei überschrieben, sondern die Namen mit _2, _3, ... erweitert.
1. **Aufnahmedatum_Anpassen**
Das Programm erstellt zuerst eine Liste aller Dateien in dem ausgewählten input Ordner und allen Unterordnern.
Bearbeitet werden nur .jpg und .jpeg Dateien, alle anderen werden ohne Anpassungen kopiert.
Alle Dateien werden im angegebenen Output Ordner mit einem Eindeutigen Namen gespeichert.
Wenn zwei Bilder den selben Namen erhalten würden, wird keine Datei überschrieben, sondern die Namen mit _2, _3, ... erweitert.
Anschließend werden die Metadaten der Datei ausgelesen und es wird versucht das Aufnahmedatum des Bildes zu ermitteln.
Wenn das Aufnahmedatum vorhanden ist, wird der angegebene Offset addiert und der neue Wert in den Metadaten des Bildes gespeichert.
1. **Name_Als_Aufnahmedatum**
Das Programm erstellt zuerst eine Liste aller Dateien in dem ausgewählten input Ordner und allen Unterordnern.
Bearbeitet werden nur .jpg und .jpeg Dateien, alle anderen werden ohne Anpassungen kopiert.
Alle Dateien werden im angegebenen Output Ordner mit einem Eindeutigen Namen gespeichert.
Wenn zwei Bilder den selben Namen erhalten würden, wird keine Datei überschrieben, sondern die Namen mit _2, _3, ... erweitert.
Zuerst wird dann geprüft ob der Dateiname des Bildes im Format YYYYMMDD_hhmmss oder YYYYMMDD ist.
Ist das der Fall, so wird das Datum und gegebenenfalls die Zeit des Namens als Aufnahmedatum in den Metadaten des Bildes gespeichert.
1. **Dateigroesse_Reduzieren**
Das Programm erstellt zuerst eine Liste aller Dateien in dem ausgewählten input Ordner und allen Unterordnern.
Wenn es sich bei einer Datei um ein .jpg oder .jpeg Bild handelt, dann wird dieses in der angegebenen Qualität im Output Ordner gespeichert.
Die Originaldateien bleiben dabei immer unverändert.
Alle anderen Dateien werden ohne Änderungen im angegebenen Output Ordner mit einem Eindeutigen Namen gespeichert.
Wenn zwei Bilder den selben Namen erhalten würden, wird keine Datei überschrieben, sondern die Namen mit _2, _3, ... erweitert.

Alle Programme konnte ich bereits erfolgreich mit Android (LG, Samsung, Huawei), iPhone (Apple), Sony Kamera, WhatsApp und GoPro Bildern testen.
