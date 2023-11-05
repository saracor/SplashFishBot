# Splash v1.0 - A WoW Classic Fishing Bot

*A simple Python script for fishing automation.*

The script detects your bobber via image detection and reels the fish in when a sound volume threshold is crossed.

Use at your own risk. Any 3rd party automation, including all types of botting, is against the TOS and may cause a ban.

The script works on my machine™ as of its release, but may or may not work for you and will not be updated/fixed.

This bot was made as an educational project. Feel free to edit it yourself to suit your needs!


## Installation

Run the following commands to install dependencies:

```
pip install pyautogui
pip install keyboard
pip install soundcard
```

## In-game configuration

```
-Untick "Enable Sound" in the Audio options
-Download 'Better Fishing' addon
-Enable 'Enhance sounds' option from the addon to 100%
-Bind your 'Fishing' spell to a keyboard button
-Have the game running on your main screen as that is where the coordinates have been set to
```

## Usage

Find a location with no other fishers as other bobbers will confuse the bot. Start the script and enjoy.

In case you are having issues with the bobber detection, you can add your own bobber screenshot(s) into the images folder as jpg files and the script will use them as well.

