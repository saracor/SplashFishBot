# Splash v1.0 - A WoW Classic Fishing Bot

*A simple Python script for fishing automation.*

The script locates your bobber via image detection and reels the fish in when a sound volume threshold is crossed.

Use at your own risk. Any 3rd party automation, including all types of botting, is against the TOS and may cause a ban.

This bot was made as an educational project and likely won't be updated after its release. Feel free to edit it yourself!


## Installation

Run the following commands to install dependencies:

```
pip install pyautogui
pip install opencv-python
pip install keyboard
pip install soundcard
```

## In-game configuration

• Enable Auto Loot if not enabled. Gameplay -> Controls -> Auto Loot

• Untick all sound options from the game Audio options, including "Enable Sounds"

• Download 'Better Fishing' addon

• Enable 'Enhance sounds' option from the addon to 100%

• Bind your 'Fishing' spell to a keyboard button


## Usage

Find a location with no other fishers as other bobbers will confuse the bot. Start the script and enjoy.
```
python splash.py
```

You have two options: 

[1] Use your default audio output device. You cannot listen to other audio while botting. No further changes needed.

[2] Use a virtual audio device if you want to enjoy other sounds while botting. If selecting this, you need to download and install VoiceMeeter, and set it as your Output Device in the game options.


If you are having issues with bobber detection due to resolution or other differences, replace the existing images with a few of your own bobber screenshots (must be .jpg). See the original files for reference.


## Troubleshooting

**Error message complaining about Pillow when running the script?**

```
pip install --upgrade Pillow
```
If this doesn't fix the issue, see Pillow documentation for supported Python versions.


**Poor bobber detection?**

Use your own bobber images for detection. See Usage section.


**Other application sounds disturbing sound detection?**

See Usage section for using a virtual audio device.
