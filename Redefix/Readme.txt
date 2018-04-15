  ______     ______     _____     ______     ______   __     __  __
 /\  == \   /\  ___\   /\  __-.  /\  ___\   /\  ___\ /\ \   /\_\_\_\
 \ \  __<   \ \  __\   \ \ \/\ \ \ \  __\   \ \  __\ \ \ \  \/_/\_\/_
  \ \_\ \_\  \ \_____\  \ \____-  \ \_____\  \ \_\    \ \_\   /\_\/\_\
   \/_/ /_/   \/_____/   \/____/   \/_____/   \/_/     \/_/   \/_/\/_/
   
   (c) Sumpfkrautjunkie 2010

   
   
 +------+
 |Inhalt|
 +------+
 1. Der Sinn des Programms
 2. Was das Programm kann
 3. Einrichten des Programms
 4. Die einzelnen Funktionen im �berblick
 5. FAQ
 6. Changelog
 
 +-------------------------+
 |1. Der Sinn des Programms|
 +-------------------------+
 
 Redefix dient dazu, die Untertitel beim Entwickeln von Gothic-Modifikationen 
 (f�r G1 und G2-DNdR) schnell und unkompliziert zu aktualisieren.
 Zwar bietet der Spacer bereits die M�glichkeit Untertitel zu aktualisieren, 
 allerdings kann man bei einer Aktualisierung durch den Spacer gerne mal eine
 Kaffeepause einplanen, da dieser unglaublich (und vor allem unn�tig) lange f�r 
 diesen Vorgang braucht. Des Weiteren ist die Handhabung der spacerseitigen 
 Aktualisierung unn�tig kompliziert. Aus diesem Grund wurde Redefix entwickelt.
 Redefix kann mit nur einem Mausklick die Untertitel in nur einem kleinen Bruchteil
 der Zeit aktualisieren, die der Spacer daf�r ben�tigt. Des Weiteren bietet er
 einige zus�tzliche Komfortfunktionen. Redefix ist �brigens nur eine stark
 optimierte und mit einer Benutzeroberfl�che ausgestattete Weiterentwicklung von
 ADOUSADS, einer etwas �lteren Software von mir :-)
	

 +------------------------+
 |2. Was das Programm kann|
 +------------------------+
 
 Redefix kann die OutputUnits aktualisieren, indem es im Cutscene-Ordner die alte
 OU.BIN l�scht und eine neue OU.CSL erstellt (oder direkt selbst eine OU.BIN erstellt), aus welcher Gothic beim n�chsten
 Start automatisch eine neue OU.BIN generiert, welche f�r die Untertitel ben�tigt
 wird. Findet Redefix Untertitel, welche zwar die gleiche Bezeichnung haben aber
 unterschiedliche Untertiteltexte, was beim Erstellen von Dialogen per Copy & Paste
 schnell mal passieren kann, so werden diese aufgelistet.
 Davon w�re z.B: betroffen:
 
 AI_Output (other, self, "DIA_Addon_Fortuno_Hi_15_02");//Alles klar bei dir?
 AI_Output (other, self, "DIA_Addon_Fortuno_Hi_15_02");//Hallo Fremder!
 
 
 Daneben gibt es die M�glichkeit, schnell die Scripte auf Syntaxfehler zu �berpr�fen,
 also, ob z.B. irgendwo eine Klammer oder ein Semikolon vergessen worden ist.
 
 Sofern man keine Sprchausgabe hat oder erstellen m�chte und sich an der imho recht bescheidenen internen
 Berechnung f�r die Anzeigedauer unvertonter Dialoge st�rt, kann sich von Redefix eine angepasste *.CSL/*.BIN
 erstellen lassen, welche stumme .WAV Dateien variabler L�nge in unvertonte Dialoge einsetzt. Damit kann man 
 die Anzeigedauer der Untertitel selber beeinflussen ohne irgendwelche st�renden Nebeneffekte.

 Mehr kann Redefix nicht.

 +---------------------------+
 |3. Einrichten des Programms|
 +---------------------------+
 
 Zum Start des Programms ist erstmal das .Net Framework 2.0 n�tig. Wird ein �lteres
 Windows als Vista verwendet, ist es unter Umst�nden nicht installiert (beim Start
 von Redefix erscheint eine Fehlermeldung). Das .Net Framework kann von der
 Microsoft-Seite heruntergeladen werden:
 http://www.microsoft.com/downloads/details.aspx?displaylang=de&FamilyID=0856eacb-4362-4b0d-8edd-aab15c5e04f5
 
 Damit das Programm arbeiten kann, ben�tigt es einige Dateipfade. Daneben k�nnen
 einige Einstellungen des Programms an die eigenen W�nsche angepasst werden.
 
 Beim ersten Start des Programms erscheint eine Fehlermeldung, dass die Datei f�r
 die Einstellungen nicht gefunden wurde. Dies ist nicht verwunderlich, denn diese
 Datei existiert ja noch gar nicht. Die Fehlermeldung kann also getrost ignoriert
 werden. Nur wenn sie sp�ter mal scheint ist sie ein Indiz daf�r, dass die Datei
 f�r die Einstellungen (die Settings.xml) versehentlich gel�scht wurde. Nach der
 Meldung wird  Automatisch das Einstellungsfenster ge�ffnet, um dort die ben�tigten
 Einstellungen angeben zu k�nnen.
 
 Die erste wichtige Einstellung ist "Pfad zum Gothic Ordner". Hier muss man den
 Pfad  zum Ordner angeben, in welchem sich Gothic befindet. Dies k�nnte z.B. der
 Pfad:
 C:\Program Files (x86)\JoWooD\Gothic II
 sein. Nat�rlich ist  es abh�ngig von den eigenen Ordnernamen und ist daher von
 Rechner zu Rechner unterschiedlich.
 
 Die zweite wichtige Einstellung ist "Zu verwendende *.Src". Damit legt man fest,
 welche  Src-Datei Redefix konsultieren soll, um die Scripte zu finden in denen
 es nach  Untertiteln suchen soll. Src-Dateien sind im Prinzip Dateilisten, welche
 die Dateien definieren, welche Gothic als Scripte betrachten soll. Sollte man
 da keine besonderen W�nsche haben, sollte man die Standard-Datei angeben, die
 "Gothic.src". Diese findet man in vom Gothic-Ordner aus gesehen in 
 _work\Data\Scripts\Content
 
 Die Einstellung "Name der zu erstellenden *.Csl/*.Bin" sollte bei ihrem Standardwert
 OU belassen werden, sofern man dahingehend keine vom Standard abweichenden
 W�nsche hat. Die Einstellung legt den Dateinamen der Csl/Bin-Datei fest, welche aus
 den gefundenen Untertiteln erstellt wird. In der Modifaktions-Ini kann n�mlich 
 der Name der Untertiteldatei angegeben werden, welche f�r die Modifikation
 verwendet werden soll. Diese Einstellung  ist standardm��ig "OU".
 
 Die Option "Erstellen" legt fest, ob eine *.Csl, eine kompilierte *.Bin oder direkt
 beide Dateien erstellt werden sollen. Wird die .Bin erstellt, muss diese nicht mehr
 von Gothic selbst erstellt werden, was prinzipiell Zeit sparen sollte.
 
 
 "Kommentare filtern" legt fest, ob Redefix beim Aktualisieren der Untertitel
 �berpr�fen soll, ob die Untertitel ggf. auskommentiert sind und daher gar nicht
 im Spiel vorkommen k�nnen. Dies kostet zwar etwas Leistung, daf�r werden aber
 keine unn�tigen Untertitel erfasst und es kommt nicht zu Problemen mit doppelt
 vorhandenen Untertiteln (die aufgrund einer Auskommentierung eigentlich einmalig
 sind). Die regul�ren Kommentare hinter AI_Output in welchen die Untertiteltexte
 stehen, sind davon NICHT betroffen.
 
 Die Option "Hotkey verwenden" legt fest, ob die Aktualisierung der Untertitel
 au�erhalb des Programms durch ein Tastenk�rzel erfolgen kann. Dies kann
 insofern praktisch sein, dass man das Redefix-Fenster nicht in den Fokus nehmen
 muss, um die Untertitel zu aktualisieren. Im nebenstehenden (nur bei gesetztem
 H�kchen sichtbaren) Feld kann die Tastenkombination festgelegt werden. Dazu muss
 das Feld erst mit der Maus angeklickt und dann die gew�nschte Tastenkombination
 gedr�ckt werden. Ab dann kann die Aktualisierungs-Funktion jederzeit  (Redefix
 muss selbstverst�ndlich gestartet sein, aber es ist egal, ob das Redefix-Fenster
 fokussiert ist oder nicht ) �ber diese Kombination aufgerufen werden. 
 

 "Variable Untertitell�nge" �ffnet ein Untermen�, in welchem man einstellen kann,
 ob und wie den unvertonten Dialogen stumme .WAVs zugewiesen werden, um die Anzeigedauer
 der Dialoge selber anzupassen.
 "Variable Untertitell�nge aktivieren" aktiviert die Erstellung und Zuordnung der stummen .WAV
 Dateien. ,
 "Buchsabe/Sekunde" legt die angenommene Lesegeschwindigkeit fest.
 "Minestl�nge" legt die Zeit in Sekunden fest f�r die die Untertitel mindestens angezeigt werden.
 "H�hstl�nge" legt die Zeit in Sekunden fest, f�r die die Untertitel h�chstens angezeigt werden.
 "L�ngenaufschlag" addiert zur errechneten Anzeigel�nge immer einen festen Wert dazu.
 Die Formel f�r die L�ngenberechnung ergibt sich aus:

	L�nge=Textl�nge/("Buchstaben/Sekunde")+L�ngenaufschlag.
	FALLS L�nge<Mindestl�nge DANN L�nge = Mindestl�nge
	FALLS L�nge>H�chstl�nge DANN L�nge = H�chstl�nge
 "Pfad zum Spech-Ordner" gibt den Ordner an, in welchem die Sprachausgabe f�r Gothic zu finden ist.
 Dort werden die stummen .Wav-Dateien hin kopiert und nach bereits vorhandenen Vertonungsdateien gesucht.
 Standardm��ig ist dieser Ordner: $Gothicordner$\_work\data\Sound\Speech

 Mit "�bernehmen" werden die Einstellungen �bernommen und gespeichert.
 
 +----------------------------------------+
 |4. Die einzelnen Funktionen im �berblick|
 +----------------------------------------+
 
 Redefix bietet zwei Hauptfunktionen zum Aktualisieren der Untertitel.
 Zum einen "Aktualisieren" und "Neu erstellen", welche beide �ber Buttons, bzw.
 die jeweiligen Kontextmen�eintr�ge des Tray-Icons erreichbar sind.
 "Neu erstellen" durchsucht alle in der *.Src aufgelisteten Scripte nach
 Untertiteln und  erstellt daraus die OU.CSL, welche Gothic f�r die Untertitel
 ben�tigt. "Aktualisieren" arbeitet �hnlich, allerdings �berpr�ft es bei jeder
 Datei, ob diese seit der letzten Aktualisierung ver�ndert wurde. Nur wenn dies
 der Fall ist, wird diese auf Untertitel untersucht, andernfalls wird sie ignoriert.
 Dies hat den Vorteil einer h�heren Geschwindigkeit, allerdings werden dabei kein
 Untertitel ber�cksichtigt, welche zwischenzeitlich gel�scht wurden. Das hei�t,
 dass die Untertiteldatei unter Umst�nden zu viele Eintr�ge haben kann, was aber
 f�r den Praxisbetrieb nicht wirklich relevant ist. Zum Erstellen der f�r den
 Release/Betatest finalen Version der Untertiteldatei sollte allerdings der
 kleineren Gr��e wegen lieber die "Neu erstellen"-Methode verwendet werden.
 �nderungen an Untertiteltexten werden in der "Aktualisieren"-Methode ber�cksichtigt
 und eingebunden, allerdings funktioniert hierbei aufgrund der speziellen 
 Arbeitsweise die Erkennung von doppelt vorhandenen Untertiteln nicht.
 Dies sollte aber f�r den Alltagsgebrauch kein allzu gro�es Problem darstellen.
 
 Die Aktualisierung kann dar�ber hinaus �ber eine Tastenkombination, welche
 man in den Einstellungen definieren kann und �ber einen Klick mit der mittleren
 Maustaste auf das Tray-Icon (das kleine Redefix-Icon im Bereich neben der Uhr)
 erfolgen.
 
 "Syntaxcheck"  �berpr�ft die Scripte auf Syntaxfehler und zeigt gefundene Fehler
 unten bei den Zusatzinfos an.
 
 "Zusatzinfos anzeigen" zeigt bzw. blendet den Bereich an/aus, in welchem
 doppelt vorhandene Untertitel oder gefundene Syntaxfehler angezeigt werden. 
 Ein einfacher Klick kopiert ihren Namen direkt in die Zwischenablage, sodass 
 man in der "Suchen in Dateien"  Funktion des Editors der eigenen Wahl schnell 
 danach suchen kann. Ein Doppelklick  hingegen �ffnet alle Scriptdateien, in 
 welchen der Name des Untertitels vorkommt. Bei Fehlern �ffnet sich direkt das
 als fehlerhaft erkannte Script und es wird die Zeilennummer mit dem Fehler in
 die Zwischenablage kopiert, damit man schnell zu der fehlerhaften Zeile navigieren
 kann (in den meisten Editoren ist es die Tastenkombination STRG+G).
 
 Beim Minimieren des Fensters verschwindet dieses aus der Taskleiste. Hervorholen
 kann man es,  indem man doppelt auf das Redefix-Tray-Icon (links neben der Uhr)
 klickt oder mit einem Rechtsklick im dortigen Kontextmen� die Option "Anzeigen"
 ausw�hlt.
 

 +------+
 |5. FAQ|
 +------+

 F: Ich habe die Untertitel mit Redefix aktualisiert, aber sie erscheinen nicht
 im Spiel.
 A: Dies kann unterschiedliche Gr�nde haben.
 
 Zuerst sollte man �berpr�fen, ob im Ordner _work\data\Scripts\Content\Cutscene
 eine neue OU.CSL erstellt wurde (auf �nderungsdatum der Datei schauen) und es 
 im Ordner keine OU.BIN mehr gibt. Ist keine neue OU.CSL erstellt worden oder
 die OU.BIN bereits vorhanden, sollte �berpr�ft werden, ob in den Redefix-
 Einstellungen auch die richtigen Pfade angegeben wurden und ob man auf diese 
 Schreibrechte hat. Dies kann bei den seltsamen Wirrungen von Windows manchmal
 sogar der Fall sein, wenn man als Administrator angemeldet ist. Die Schreibrechte
 eines Ordners kann man in den  Ordnereigenschaften (Rechtsklick auf den Ordner 
 -> Eigenschaften) unter dem Reiter "Sicherheit" einstellen.  Allgemein empfiehlt
 es sich, Gothic unter Vista nicht in den Ordner "C:\Programme" zu installieren,
 da dort andere Sicherheitsbestimmungen gelten, als in anderen Ordnern. Geeigneter
 w�re ein  Installationsort z.B. in einem Ordner "C:\Spiele".
 
 Sollte eine neue OU.CSL erstellt worden sein, kann das Ausbleiben der Untertitel
 an der Modifikations-Ini-Datei liegen, �ber die man die Mod im GothicStarter
 startet. Diese darf keinen VDF= Eintrag haben, da sonst nicht die aktuell erstellten
 Untertitel verwendet werden. So hat man in der GothicGame.ini z.B. standardm��ig
 einen Eintrag bei VDF=, welcher  unter anderem zu den Originaluntertiteln f�hrt.
 Eine m�gliche L�sung w�re es, die GothicGame.ini im Gothic-System-Ordner zu �ffnen
 und dort bei der Zeile 
 VDF=GothicGame.mod
 den Rest der Zeile hinter dem = zu l�schen:
 VDF=
 
 Eleganter w�re es eine eigene .ini Datei zu erstellen, denn darum kommt man,
 wenn man irgendwann die Mod ver�ffentlichen m�chte nicht herum. Dazu kopiert
 man einfach die GothicGame.ini im Systemverzeichnis und benennt die Datei um,
 z.B. in: DarkIsland.ini (am besten ist es, wenn der Name etwas mit dem Titel
 der Mod zu tun hat :-) )
 Dann �ffnet man diese Datei und passt sie den eigenen W�nschen entsprechend an.
 Zuallererst sollte, wie oben beschrieben erstmal der Eintrag hinter VDF= gel�scht
 werden. Eine fertig  eigene Ini k�nnte so aussehen:

	[INFO]
	Title=Die Dunkle Insel
	Version=1.0
	Authors=Ich und Ich
	Webpage=http://www.meinewebseite123344.de
	Description=!<symlink>DarkIsland.rtf
	Icon=GothicStarter.exe

	[FILES]
	VDF=
	Game=Content\Gothic
	FightAI=Content\Fight
	Menu=System\Menu
	Camera=System\Camera
	Music=System\Music
	SoundEffects=System\SFX
	ParticleEffects=System\ParticleFX
	VisualEffects=System\VisualFX
	OutputUnits=OU

	[SETTINGS]
	Player=PC_HERO
	World=NewWorld\NewWorld.zen

	[OPTIONS]
	show_Info=0
	show_InfoX=800
	show_InfoY=7200
	show_Version=1
	show_VersionX=6500
	show_VersionY=7200
	show_Focus=1
	show_FocusItm=1
	show_FocusMob=1
	show_FocusNpc=1
	show_FocusBar=1
	force_Subtitles=0
	force_Parameters=

	[OVERRIDES]
	INTERNAL.extendedMenu=1
 
 
 Description verweist auf eine Datei in der die Modbeschreibung zu finden ist
 (der Text wird sp�ter beim Spieler angezeigt). Diese kann erstellt werden, 
 indem die GothicGame.rtf kopiert, umbenannt und inhaltlich z.B. mit dem
 Windowsprogramm "Wordpad" ver�ndert wird. Bei Icon kann man ein eigenes Symbol
 angeben, mit welchem die Mod im Gothicstarter abgebildet wird. Die Einstellung
 World legt die Startwelt der Mod fest. Dies ist eine Angabe vom Ordner
 _work\data\Worlds aus gesehen. Sollte die Mod in der gleichen Welt, wie Gothic 2
 spielen, ist hier keine �nderung n�tig. Die restlichen Angaben au�erhalb der
 INFO-Sektion sollten (f�r den Anfang) nicht ver�ndert werden.
 
 
 F: Redefix ist mir zu langsam, geht's schneller?
 A: Wer Lust hat, kann eine native C/C++ Version schreiben :P
 Ansonsten kann man einige Optimierungen vornehmen, wie auf das Filtern von 
 Kommentaren verzichten und eine optimierte *.Src verwenden. Diese sollte nur
 Dateien beinhalten, in welchen auch wirklich Untertitel zu finden sind. So 
 kann man im Content-Ordner eine eigene *.Src nur f�r Redefix anlegen,
 welche z.B. den Inhalt hat:
 
 STORY\svm.d
 STORY\DIALOGE\DIA*.d
 STORY\B_AssignAmbientInfos\*.d

 Dadurch muss Redefix deutlich weniger Dateien abarbeiten, was eine
 Aktualisierung deutlich beschleunigt.
 
 F: Die Tastenkombination einer anderen Anwendung, die ich verwende, funktioniert
 nicht, wenn Redefix l�uft. 
 A: Die Hotkeyfunktion von Redefix kann in den Einstellungen deaktiviert oder
 umbelegt werden.
 
 F: Redefix startet nicht, es kommt eine Fehlermeldung
 A: Wenn ein �lteres Windows verwendet wird, als Vista, kann es durchaus sein,
 dass das zum Start des Programms ben�tigte .Net Framework 2.0 nicht installiert
 ist (bei Vista ist es schon vorinstalliert). Das .Net Framwork kann  von der
 Microsoft-Seite heruntergeladen werden:
 http://www.microsoft.com/downloads/details.aspx?displaylang=de&FamilyID=0856eacb-4362-4b0d-8edd-aab15c5e04f5
 
 F: Warum muss ich das ".Net Framework" installieren?
 A: Aus dem selben Grund, warum man z.B. Flash, Python, Java oder Visual C++ 2005
 Redistributable Packages installiert. Manche Software ben�tigt einfach bestimmte
 Dateien um zu funktionieren. Bei Redefix ist es die .Net  Laufzeitumgebung und
 die .Net Bibliotheken. Analog �bertragen: Ohne Back�fen in den Haushalten w�ren
 Tiefk�hlpizzen ziemlich sinnlos :-)
 
 +------------+
 |6. Changelog|
 +------------+
 
 # 1.4
 Bugfixes:
 - UNIX - Formatierte Scriptdateien sollten jetzt korrekt gelesen werden k�nnen
 - Fehler, dass die letzte OU im Script manchmal �bersehen wurde, behoben
 
 Neues:
 - Interface�nderungen
 - Optionale Syntax�berpr�fung der Scripte
 
 # 1.9
 Bugfixes:
 - Unix-Formatierte Svm.d sollte nun erkannt werden
 - Fehler, dass die letzte OU im Script manchmal �bersehen wurde, nun hoffentlich endlich behoben
 - Fehler bei Kommentarerkennung behoben
 
Neues:
 - M�glichkeit, direkt die .Bin Datei zu generieren


# 2.0
Neues:
 - Neues Icon
 - M�glichkeit, die Anzeigedauer von unvertonten Dialogen einzustellen (�hnlich Sektenspinners B.lang.loS )

# 2.1
Bugfixes:
 -.src Angaben in .src Dateien werden nun erkannt