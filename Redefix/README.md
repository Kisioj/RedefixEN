```
  ______     ______     _____     ______     ______   __     __  __
 /\  == \   /\  ___\   /\  __-.  /\  ___\   /\  ___\ /\ \   /\_\_\_\
 \ \  __<   \ \  __\   \ \ \/\ \ \ \  __\   \ \  __\ \ \ \  \/_/\_\/_
  \ \_\ \_\  \ \_____\  \ \____-  \ \_____\  \ \_\    \ \_\   /\_\/\_\
   \/_/ /_/   \/_____/   \/____/   \/_____/   \/_/     \/_/   \/_/\/_/
   
   (c) Sumpfkrautjunkie 2010
   translated by google translate in 2018
```
   
   
## Content
##### 1. The meaning of the program
##### 2. What the program can do
##### 3. Setting up the program
##### 4. The individual functions at a glance
##### 5. FAQ
##### 6. changelog
 
### 1. The meaning of the program

Redefix is used to develop subtitles when developing gothic modifications
  (for G1 and G2-NotR) update quickly and easily.
  Although the spacer already offers the possibility to update subtitles,
  However, you can with an update by the spacer like a time
  Schedule a coffee break, as this is unbelievable (and above all unnecessary) for a long time
  this process needs. Furthermore, the handling of the spacer side
  Updating unnecessarily complicated. That's why Redefix was developed.
  Redefix can do the subtitles in just a small fraction with just a click of a mouse
  update the time the spacer needs for it. Furthermore, he offers
  some additional comfort features. Incidentally, Redefix is only one strong
  optimized and user-friendly development of
  ADOUSADS, a slightly older software from me :-)

### 2. What the program can do
 
Redefix can update the OutputUnits by putting the old ones in the Cutscene folder
 OU.BIN deletes and creates a new OU.CSL (or even creates an OU.BIN itself), from which gothic the next
 Start automatically generates a new OU.BIN, which is needed for the subtitles
 becomes. Find Redefix subtitles, which have the same name but
 different subtitle texts, which when creating dialogs by copy & paste
 can happen quickly, so these are listed.
 This would be affected, for example:

```
AI_Output (other, self, "DIA_Addon_Fortuno_Hi_15_02") // Alright with you?
AI_Output (other, self, "DIA_Addon_Fortuno_Hi_15_02") // Hello stranger!
```


In addition, there is the possibility to quickly check the scripts for syntax errors,
 So, whether, e.g. somewhere a bracket or a semicolon has been forgotten.
 

Unless you have no speech or want to create and at the imho quite modest internal
 If the calculation of the display duration of unconverted dialogues is annoying, Redefix may adapt *.CSL / *.BIN
 create mute .WAV variable-length files in unvertured dialogs. You can do that
 The display duration of the subtitles themselves influence without any annoying side effects.

 Redefix can not do more.

 ### 3. Setting up the program
 
To start the program, first the .Net Framework 2.0 is necessary. Becomes an older one
 Windows is used as Vista, it may not be installed (at startup
 an error message appears from Redefix). The .Net Framework can be used by the
 Microsoft page can be downloaded:
 http://www.microsoft.com/downloads/details.aspx?displaylang=de&FamilyID=0856eacb-4362-4b0d-8edd-aab15c5e04f5
 

For the program to work, it needs some file paths. In addition, you can
 some settings of the program can be adapted to your own wishes.
 

When starting the program for the first time, an error message appears stating that the file is for
 the settings were not found. This is not surprising, because this
 File does not exist yet. The error message can safely be ignored
 become. Only if she shines later is she an indication that the file
 for the settings (the Settings.xml) was accidentally deleted. After
 Message is automatically opened the settings window to get the needed
 To specify settings.
 

The first important setting is "Path to the Gothic folder". Here you have the
 Specify the path to the folder in which Gothic is located. This could e.g. of the
 Path:
 C: \ Program Files (x86) \ JoWooD \ Gothic II
 be. Of course it depends on your own folder name and is therefore of
 Calculator to calculator different.
 

The second important setting is "* .Src" to use. This one determines
 which Src file Redefix should consult to find the scripts in which
 it should search for subtitles. Src files are basically file lists which
 Define the files, which Gothic should consider as scripts. Should
 there are no special requests, you should specify the default file, the
 "Gothic.src". These can be found in the gothic folder in
 _work \ Data \ Scripts \ Content
 

The setting "Name of the * .Csl / *. Bin" to create should be at its default value
 OU, if one does not deviate from the standard
 Wishes has. The setting specifies the filename of the csl / bin file, which is
 created subtitles is created. Namely, in the modifaction ini
 the name of the subtitle file can be specified, which for the modification
 should be used. This setting is "OU" by default.
 

The option "Create" determines whether a * .Csl, a compiled * .Bin or directly
 both files should be created. If the .Bin is created, it does not have to
 created by Gothic itself, which should save time in principle.
 
 

"Filter Comments" determines whether or not Redefix updates the subtitles
 check whether the subtitles are commented out if necessary and therefore not at all
 can occur in the game. Although this costs a bit of power, but will be
 No unnecessary subtitles are recorded and there are no double problems
 existing subtitles (which are actually unique due to commenting out)
 are). The regular comments behind AI_Output in which the subtitle texts
 are not affected.
 

The "Use Hotkey" option determines whether to update the subtitles
 can be done outside the program by a shortcut. This can
 be practical in that you do not focus on the redefix window
 needs to update the subtitles. In the opposite (only when set
 Check mark visible) box, the keyboard shortcut can be set. This must be
 first click on the field with the mouse and then the desired key combination
 be pressed. From then on, the update feature can be used at any time (Redefix
 must of course be started, but it does not matter if the redefix window
 focused or not) are called via this combination.
 


"Variable subtitle length" opens a submenu in which you can set
 whether and how the unconverted dialogs are muted .WAVs assigned to the display duration
 adapt the dialogues yourself.
 "Enable variable subtitle length" activates the creation and assignment of the mute .WAV
 Files. .
 "Read / Second" sets the assumed reading speed.
 "Minestlength" defines the time in seconds for which the subtitles are at least displayed.
 "Highest Length" sets the time in seconds for which the subtitles are displayed at most.
 "Length surcharge" always adds a fixed value to the calculated display length.
 The formula for the length calculation results from:

```
Length = Text length / ( "Letters / second") + length surcharge.
IF length <minimum length THEN length = minimum length
IF length> maximum length THEN length = maximum length
```


"Path to the Spech folder" indicates the folder in which the speech output for Gothic can be found.
 There, the mute .Wav files are copied out and searched for existing sound files.
 By default, this folder is $ Gothicfolder $ \ _ work \ data \ Sound \ Speech


With "Apply" the settings are accepted and saved.
 
### 4. The individual functions at a glance
 

Redefix offers two main functions for updating subtitles.
 On the one hand "update" and "create new", which both via buttons, or
 the respective context menu entries of the tray icon are accessible.
 "Rebuild" searches all scripts listed in the * .Src
 Subtitles and creates the OU.CSL, which Gothic for the subtitles
 needed. "Refresh" works similarly, but it checks at each
 File, if this was changed since the last update. Only if this
 If this is the case, it will be examined for subtitles, otherwise it will be ignored.
 This has the advantage of a higher speed, but no
 Subtitles that have been deleted in the meantime. This means,
 that the subtitle file may have too many entries, but what
 is not really relevant for the practice. To create the for the
 Release / beta test final version of the subtitle file, however, should be the
 smaller size because of the "Rebuild" method.
 Changes to subtitle texts are reflected in the "Refresh" method
 and integrated, but this works because of the special
 Operation does not detect duplicate subtitles.
 However, this should not be too big a problem for everyday use.
 

The update may also have a keyboard shortcut which
 one can define in the attitudes and over one click with the middle one
 Click on the tray icon (the small redefix icon next to the clock)
 respectively.
 

"Syntaxcheck" checks the scripts for syntax errors and shows found bugs
 below at the additional information.
 

"Show additional info" shows / hides the area on / off in which
 duplicate subtitles or found syntax errors are displayed.
 A simple click copies its name directly to the clipboard, so that
 one in the "Search in Files" function of the editor of your own choice quickly
 can search for it. A doubleclick on the other hand opens all script files, in
 which contains the name of the subtitle. In the case of errors, this opens directly
 as erroneously recognized script and it becomes the line number with the error in
 Copied the clipboard to quickly navigate to the faulty line
 can (in most editors it is the key combination CTRL + G).
 

Minimizing the window disappears from the taskbar. prefetching
 you can do it by double-clicking the redefix tray icon (left of the clock)
 click or with a right-click in the local context menu the option "Show"
 selects.
 
### 5. FAQ

Q: I've updated the subtitles with Redefix, but they are not appearing
 in the game.

A: This can have different reasons.
 

First you should check if in the folder _work \ data \ Scripts \ Content \ Cutscene
 a new OU.CSL was created (look at the modification date of the file) and it
 in the folder no OU.BIN gives more. No new OU.CSL has been created or
 the OU.BIN already exists, it should be checked whether in the Redefix
 Settings also the correct paths were specified and whether one on these
 Has write permission. This can sometimes be the case with the strange confusions of Windows
 even be logged in as an administrator. The write rights
 of a folder can be found in the folder properties (right-click on the folder
 -> Properties) under the "Security" tab. Generally recommended
 it is, Gothic under Vista not to install in the folder "C: \ Program Files",
 because there are different security rules than in other folders. suitable
 would be an installation location e.g. in a folder called "C: \ Games".
 

If a new OU.CSL has been created, the lack of subtitles can
 at the modification ini file, over which one the mod in the GothicStarter
 starts. This may not have a VDF = entry, otherwise not the currently created
 Subtitles are used. So you have in the GothicGame.ini, for example By default
 an entry in VDF =, which leads among other things to the original subtitles.
 A possible solution would be to open the GothicGame.ini in the Gothic system folder
 and there at the line
 VDF = GothicGame.mod
 to delete the rest of the line after the =:
 VDF =
 

It would be more elegant to create your own .ini file, because that's the point
 if you do not want to publish the mod at some point Copied to it
 just drop the GothicGame.ini in the system directory and rename the file,
 e.g. in: DarkIsland.ini (it is best if the name is something titled
 the mod has to do :-))
 Then open this file and adjust it according to your own wishes.
 First and foremost, as described above, the entry after VDF = should first be deleted
 become. A finished own Ini could look like this:

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
 
 
Description refers to a file in which the mod description can be found
 (the text will be shown later to the player). This can be created
 by copying, renaming and contenting the GothicGame.rtf e.g. with the
 Windows program "Wordpad" is changed. With Icon you can create your own symbol
 specify, with which the mod in the Goth starter is mapped. The setting
 World determines the start world of the mod. This is an indication of the folder
 _work \ data \ Worlds seen from. Should the mod in the same world as Gothic 2
 play, no change is necessary here. The remaining information outside the
 INFO section should not be changed (for starters).
 
 

Q: Redefix is ​​too slow for me, is it faster?

A: If you feel like it, you can write a native C / C ++ version :P
Otherwise you can do some optimizations, like filtering on
 Forgo comments and use an optimized * .Src. This should only
 Include files in which subtitles can be found. So
 you can create your own * .Src in the content folder only for Redefix,
 which e.g. the content has:

```
 STORY \ svm.d
 STORY \ Dialogues \ DIA * .d
 STORY \ B_AssignAmbientInfos \ * d.
```

As a result, Redefix has to process significantly fewer files, which is one thing
 Update significantly accelerated.
 

Q: The keyboard shortcut of another application I use works fine
 not when Redefix is ​​running.

A: The hotkey feature of Redefix can be disabled in the settings or
 be transferred.
 

Q: Redefix does not start, there is an error message

A: If an older Windows is used than Vista, it may well be
 that the .Net Framework 2.0 needed to start the program is not installed
 is (in Vista it is already preinstalled). The .Net framwork can be done by the
 Microsoft page can be downloaded:
 http://www.microsoft.com/downloads/details.aspx?displaylang=de&FamilyID=0856eacb-4362-4b0d-8edd-aab15c5e04f5
 

Q: Why do I have to install the ".Net Framework"?

A: For the same reason why you e.g. Flash, Python, Java or Visual C ++ 2005
 Redistributable Packages installed. Some software just needs certain
 Files to work. For Redefix, it is the .NET runtime environment and
 the .Net libraries. Analog transmitted: Without ovens in the households would be
 Frozen pizzas pretty pointless :-)
 
### 6. changelog
 
# 1.4
bug fixes:
 - UNIX - Formatted script files should now be able to be read correctly
 - bug that the last OU in the script was sometimes overlooked fixed

new:
 - Interface changes
 - Optional syntax check of the scripts

 # 1.9
bug fixes:
 - Unix-formatted Svm.d should now be recognized
 - Error that the last OU in the script was sometimes overlooked, hopefully finally fixed
 - Bug in comment detection fixed

new:
 - Possibility to directly generate the .Bin file


# 2.0
new:
 - New icon
 - Possibility to set the display duration of unconverted dialogues (similar to Sektenspinners B.lang.loS)

# 2.1
bug fixes:
 -src data in .src files are now recognized