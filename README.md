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

```
• Untick "Enable Sound" in the game Audio options
• Download 'Better Fishing' addon
• Enable 'Enhance sounds' option from the addon to 100%
• Bind your 'Fishing' spell to a keyboard button
• Disable guild member alert via Interface -> Social -> Guild Member Alert

```

## Usage

Find a location with no other fishers as other bobbers will confuse the bot. Start the script and enjoy.

If you are having issues with bobber detection, replace the existing bobber images with your own bobber screenshots (must be .jpg). See the original files for reference.


## Troubleshooting

Error message complaining about Pillow?
```
pip install --upgrade Pillow
```
If this doesn't fix the issue, see Pillow documentation for supported Python versions.

Poor bobber detection?
```
Use your own bobber images for detection. See Usage section.
```

Other sounds disturbing sound recognition?
```
Mute other apps via your operating system's sound settings.
```