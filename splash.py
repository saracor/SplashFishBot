import pyautogui, time, keyboard, os
import numpy as np
import soundcard as sc


def cast_line():
    time.sleep(np.random.uniform(0.3,0.6))
    pyautogui.keyDown(f'{castingkey}')
    time.sleep(np.random.uniform(0.1,0.3))
    pyautogui.keyUp(f'{castingkey}')
    

def find_bob():
    global bob_found
    current_dir = os.getcwd()
    bob_directory = f"{current_dir}\images"

    while True:
        print("<< Looking for Bob. Hold esc to quit. >>")
        bob_found = False
        time.sleep(np.random.uniform(0.6,1.2))

        if keyboard.is_pressed('esc') == True:
            print("<< Exiting >>")
            exit()

        for file in os.listdir(bob_directory):
            if file.endswith(".jpg"):
                file = (f"{bob_directory}\{file}")
                screen_loc = pyautogui.locateOnScreen(file, confidence=0.6, grayscale=True, region=(650,350, 1300, 800))
                if screen_loc:
                    screen_loc = pyautogui.center(screen_loc)
                    print("<< Moving to bob... >>")
                    pyautogui.moveTo(screen_loc.x, screen_loc.y, np.random.uniform(0.4,1.1), pyautogui.easeOutQuad)
                    bob_found = True
                    break
        break


def reel_in():
    seconds_timer = 0
    global reeled

    while True:
        reeled = False

        if keyboard.is_pressed('esc') == True:
            print("<< Exiting >>")
            exit()

        audio_source = sc.default_speaker().name
        mic = sc.get_microphone(id=audio_source, include_loopback=True)
        data = mic.record(samplerate=44100, numframes=44100)
        audio_peak = np.max(abs(data))
        seconds_timer += 1

        if audio_peak > 0.06:
            print("<< You (hopefully) caught something! >>\n")
            time.sleep(np.random.uniform(0.05,0.12))
            pyautogui.mouseDown(button='right')
            time.sleep(np.random.uniform(0.05,0.12))
            pyautogui.mouseUp(button='right')
            time.sleep(np.random.uniform(0.35,0.5))
            reeled = True
            break

        if seconds_timer > 13:
            print("<< Failed. Trying again. >>")
            break
 

if __name__ == "__main__":
    print(
        '''
       .
      ":"
    ___:____     |"\/"|
  ,'        `.    \  /
  |  O        \___/  |
~^~^~^~^~^~^~^~^~^~^~^~^~
Splash splash v1.0.                                           
    '''
    )

    global castingkey
    print()
    castingkey = input("Input your casting key or type exit to quit the program > ")
    castingkey = castingkey.lower()
    if castingkey == 'exit':
        exit()
    else:
        print("\nStarting in 10 seconds. Activate the correct window.")
        time.sleep(7)
        print("\n3")
        time.sleep(1)
        print("2")
        time.sleep(1)
        print("1\n")
        time.sleep(1)

    while True:
        if keyboard.is_pressed('esc') == True:
            print("<< Exiting >>")
            exit()

        print("\n<< Casting >>")
        cast_line()
        find_bob()
        if bob_found:
            reel_in()
            if reeled:
                continue
        else:
            time.sleep(np.random.uniform(2.3,4.7))
            continue

        





