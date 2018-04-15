import os
import sys

DE_2_EN = {
    'Aktualisieren': 'Update',
    'Neu erstellen': 'Create new',
    'Zusatzinfos anzeigen': 'Show additional info',
    'Doppelt:': 'Duplic.:',  # Duplicates
    'Einstellungen': 'Settings',
    'Erstellen:': 'Create:',
    'Fehler:': 'Error:',
    'Pfad zum Gothic Ordner:': 'Path to Gothic folder:',
    'Src-Dateien|*.src': 'src-file|*.src',
    'Zu verwendende *.Src:': '*.src file to use:',
    'Name der zu erstellenden *.Csl/*.Bin:': 'Name of the *.csl/*.bin file:',
    'Übernehmen': 'Accept',
    'Schließen': 'Close',
    'Kommentare filtern': 'Filter comments',
    'Hotkey verwenden': 'Hotkey used',
    'Variable Untertitellänge': 'Variable subtitle length',
    'Abbrechen': 'Cancel',
    'Variable Untertitellänge aktivieren': 'Enable variable subtitle length',
    'Buchstaben/Sekunde': 'Chars per second',
    'Mindestlänge (Sek)': 'Min length (secs)',
    'Höchstlänge (Sek)': 'Max length (secs)',
    'Längenaufschlag': 'Base length',
    (
        'Addiert zur errechneten Zeit immer einen festen Wert dazu.\r\n'
        'Die Schranken der Höchst- und Mindestlänge wirken weiterhin'
    ): (
        'Add a fixed value at the calculate time.\r\n'
        'The barriers of maximum and minimum length continue to be effective.'
    ),
    (
        'Die erwartete Lesegeschwindigkeit.\r\n'
        'Die Länge der Anzeigedauer berechnet sich aus \r\nTextlänge / diesem Wert'
    ): (
        'The expected reading speed.\r\n'
        'The length of the display duration is calculated from text length / this value'
    ),
    (
        'Die minimale Anzeigedauer eines Dialogs. Ist der errechnete Wert kleiner, so wird dieser\r\n'
        'automatisch auf diesen Wert gesetzt.'
    ): (
        'The minimum display duration of a dialog. If the calculated value is smaller, it is\r\n'
        'automatically set to this value.'
    ),
    (
        'Die maximale Anzeigedauer eines Dialogs. Ist der errechnete Wert größer, so wird dieser\r\n'
        'automatisch auf diesen Wert gesetzt.'
    ): (
        'The maximum display duration of a dialog. If the calculated value is greater, it is\r\n'
        'automatically set to this value.'
    ),
    (
        '@Der Pfad, in dem sich die Sprachdateien von Gothic befinden.\r\n'
        'StandardmĂ¤Ăźig: $GothicOrdner$\_work\data\Sound\Speech\r\n'
        'Dorthin werden die stillen .Wav Dateien bei Bedarf kopiert und dort wird auch nach bereits\r\n'
        'vorhandenen Dialogvertonungen gesucht.'
    ): (
        "@The path where Gothic's speech files are located.\r\n"
        'By default: $GothicFolder$\_work\data\Sound\Speech\r\n'
        'There, the silent .wav files are copied as needed and there is also\r\n'
        'searching for existing dialog dubbing.'
    ),
    (
        '@Ist die Option aktiv, so wird, falls noch keine Vertonungsdatei existiert, '
        'eine stumme .WAV dem Dialog zugewiesen.\r\n'
        'Dies hebelt die interne Anzeigedauerberechnung fĂĽr unvertonte Dialoge aus, '
        'da stumme Dialogausgaben variabler LĂ¤nge abgespielt werden.\r\n'
        'Sinnvoll, wenn man ohne fertige Sprachausgabe testen oder die Mod ohne Spachausgabe verĂ¶ffentlichen mĂ¶chte.'
    ): (
        '@If the option is active, a silent .WAV will be assigned to the dialog, if no sound file exists yet.\r\n'
        'This eliminates the internal display duration calculation for unvertured dialogs, '
        'since dumb dialog outputs of variable length are played.\r\n'
        'Useful if you want to test without finished speech output or publish the mod without voices.'
    ),
    (
        'Legt fest, ob Untertitel, welche auskommentiert sind, ignoriert werden sollen.\r\n'
        'Zwar kostet diese Option Leistung, dafür werden aber auch keine unnötigen Untertitel erfasst.'
    ): (
        'Determines whether subtitles that are commented out should be ignored.\r\n'
        'Although this option costs performance, no unnecessary subtitles are recorded.'
    ),
    (
        'Einstellung, ob die *.Csl, die *.Bin oder beide erstellt werden sollen.'
    ): (
        'Setting whether the * .Csl, * .Bin or both should be created.'
    ),
    (
        'Hier muss der Pfad zum Gothicordner angegeben werden,\r\nalso z.B. zum Ordner "Gothic II" .'
    ): (
        'Here, the path to the Gothic folder must be specified, eg. the folder "Gothic II".'
    ),
    (
        'Hier muss die *.Src angegeben werden, in welcher die Scripte aufgelistet sind,\r\n'
        'die durchsucht werden sollen. In der Regel ist es die Gothic.src.'
    ): (
        "*.src file must be specified. All scripts listened inside it will be searched.\r\n"
        "Usually it's the Gothic.src."
    ),
    'Pfad zum Speech-Ordner': 'Path to Speech folder',
    'Pfad zum Stumm-Ordner': 'Path to mute folder',
    (
        'Pfad für einen optionalen (Unter)ordner, in welchem die erstellten stummen .wav Dateien abgelegt werden.'
    ): (
        'Path for an optional (sub) folder in which the created mute .wav files are stored.'
    ),
    (
        '@Nur seit der letzten Aktualisierung verĂ¤nderte Scripte werden auf neue Untertitel durchsucht.\r\n'
        'Diese Methode ist deutlich schneller, allerdings funktioniert damit sowohl das Auffinden von \r\n'
        'doppelten Untertiteln, als auch das Entfernen nicht mehr verwendeter Untertitel nicht.\r\n'
        'Die Aktualisierung kann alternativ mit einem Hotkey ausgefĂĽhrt werden.'
    ): (
        '@Only scripts modified since the last update will be searched for new subtitles.\r\n'
        'This method is much faster, but it does not work for finding duplicate subtitles or \r\n'
        'removing unused subtitles. The update can alternatively be performed with a hotkey.'
    ),
    (
        '@Erstellt mit Hilfe der angegebenen .Src und dem Pfad zum Gothic Ordner anhand\r\n'
        'der Scripte eine OU.CSL im Cutscene-Ordner, aus welcher Gothic beim nĂ¤chsten \r\n'
        'Start automatisch die fĂĽr die Untertitel benĂ¶tigte OU.BIN generiert.\r\n'
        'Dabei werden OUs, welche doppelt vorhanden sind, aber unterschiedliche \r\n'
        'Untertiteltexte haben, aufgelistet.'
    ): (
        '@Creates OU.CSL in the Cutscene folder using the given .Src and the path to the Gothic folder.\r\n'
        'When Gothic starts, it will automatically generate the OU.BIN needed for the subtitles.\r\n'
        'Program will list OUs that are duplicated but have different subtitle texts.'
    ),
    (
        '@Blendet die Anzeige fĂĽr zusĂ¤tzliche Informationen ein bzw. aus.\r\n'
        'Dazu zĂ¤hlen doppelte Untertitel und gefundene Syntaxfehler.\r\n'
        'Die doppelten Untertitel werden in jedem Fall in die Datei "Doppelt.txt"\r\n'
        'im Redefix-Programmordner geschrieben.'
    ): (
        '@Shows or hides the display for additional information.\r\n'
        'These include duplicate subtitles and found syntax errors.\r\n'
        'The duplicate subtitles will always be written to the "Duplica.txt"\r\n'
        'file in the Redefix program folder.'
    ),
    (
        'Legt den Dateinamen  der *.Csl/*.Bin fest.\r\n'
        'Es empfiehlt sich den Standardwert OU beizubehalten (außer man weiß, was man tut).'
    ): (
        'Defines the filename of the *.Csl/*.Bin.\r\n'
        'It is recommended to keep the default value OU (unless you know what you are doing).'
    ),
    (
        'Wenn Sie das Programm zum ersten Mal starten, können Sie diese Meldung ignorieren.'
    ): (
        'When you start the program for the first time, you can ignore this message.'
    ),
    (
        '@Zeigt die doppelten OU-EintrĂ¤ge an.\r\n'
        'Ein Klick aif ein Element kopiert den Namen des Elementes in die Zwischenablage.\r\n'
        'Ein Doppelklick Ă¶ffnet zusĂ¤tzlich alle Script-Dateien, in dem das Element vorkommt.'
    ): (
        '@Displays the duplicate OU entries.\r\n'
        'One click on an item copies the name of the item to the clipboard.\r\n'
        'A double-click additionally opens all script files in which the element occurs.'
    ),
    'Bitte den Gothic-Ordner auswählen': 'Please select the gothic folder',
    'CSL und BIN': 'CSL and BIN',
    'Bestimmt, ob ein Hotkey verwendet werden soll': 'Determines if a hotkey should be used.',
    'Alle Textfelder müssen ausgefüllt sein!': 'All text fields must be filled!',
    'Fehler': 'Error',
    'Gothic-Verzeichnis existiert nicht: ': "Gothic directory does't exist: ",
    'Src exisitert nicht: ': "src doesn't exist: ",
    'Gothic-Ordner nicht gefunden:': 'Gothic folder not found: ',
    'Hier können Einstellungen vorgenommen werden.': 'Settings can be changed here.',
    'Anzahl der gefundenen doppelten Untertitel bzw. Fehler': 'Number of found duplicate subtitles or errors',
    'Doppelt.txt': 'Duplica.txt',
    'Hier kann man den gewünschten Hotkey einstellen.': 'Here you can set the desired hotkey.',
    'Dateifehler': 'File error',
    '#Untertitel: ': '# Subtitles: ',
    '#Zeit: ': '#Time: ',
    '#erwartet': '#expected',
    'Der Pfad zum Stumm-Ordner ist ungültig!': 'The path to the mute folder is invalid!',
    'Der Pfad zum Speech-Ordner ist ungültig!': 'The path to the Speech folder is invalid!',
}


def t2h(text):
    print(''.join([f'''{repr(x).strip("'"):6s}''' for x in text]))
    print(' 0x00 '.join([f'{ord(x):02x}' for x in text]).replace('0x', '').upper())


def text_2_redefix_bytes(text, encoding='windows-1250'):
    if text.startswith('@'):
        return b''.join(char.encode(encoding) for char in text[1:])
    elif text.startswith('#'):
        return b'\x00'.join(char.encode(encoding) for char in text[1:]) + b'\x00'

    return b'\x00'.join(char.encode(encoding) for char in text) + b'\x00'


def main(filename):
    with open(filename, 'rb') as file:
        content = bytearray(file.read())

    translation_map = sorted(DE_2_EN.items(), key=lambda pair: -len(pair[0]))
    for original_text, translated_text in translation_map:
        original_bytes = text_2_redefix_bytes(original_text)
        if original_bytes not in content:
            print(f'Did not find "{original_text}"')
            continue

        while original_bytes in content:
            translated_text = translated_text[:len(original_text)]  # translated text cannot be longer than original
            translated_bytes = text_2_redefix_bytes(translated_text)

            start_index = content.index(original_bytes)
            end_index = start_index + len(translated_bytes)

            if original_text.startswith('@') or original_text.startswith('#') or len(original_bytes) > 255:
                content[end_index] = 0
            else:
                len_index = start_index - 1
                content[len_index] = len(translated_bytes)

            content[start_index:end_index] = translated_bytes

    base_filename, extension = os.path.splitext(filename)
    with open(f'{base_filename} EN{extension}', 'wb') as file:
        file.write(content)


if __name__ == '__main__':
    main(filename=sys.argv[1])
