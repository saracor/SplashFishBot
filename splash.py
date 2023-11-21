import pyautogui, time, keyboard, os
import numpy as np
import soundcard as sc


def cast_line():
    time.sleep(np.random.uniform(0.3,0.55))
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
        time.sleep(np.random.uniform(1.3,1.7))

        if keyboard.is_pressed('esc') == True:
            print("<< Exiting >>")
            exit()

        try:
            for file in os.listdir(bob_directory):
                if file.endswith(".jpg"):
                    file = (f"{bob_directory}\{file}")
                    screen_loc = pyautogui.locateOnScreen(file, confidence=0.7, grayscale=True)
                    if screen_loc:
                        screen_loc_offset = ((screen_loc[0] + int(screen_loc[2] / 2) + np.random.uniform(-3,3)), (screen_loc[1] + int(screen_loc[3] / 2)) + np.random.uniform(-3,3))
                        print("<< Moving to bob... >>")
                        pyautogui.moveTo(screen_loc_offset[0], screen_loc_offset[1], np.random.uniform(0.4,1.1), pyautogui.easeOutQuad)
                        bob_found = True
                        break
        except pyautogui.ImageNotFoundException:
            pass
        break


def reel_in():
    seconds_timer = 0
    global reeled

    while True:
        reeled = False

        if keyboard.is_pressed('esc') == True:
            print("<< Exiting >>")
            exit()
        if input_device == '1':
            audio_source = sc.default_speaker().name
        if input_device == '2':
            audio_source = sc.get_speaker('VoiceMeeter Input').name
        mic = sc.get_microphone(id=audio_source, include_loopback=True)
        data = mic.record(samplerate=48000, numframes=48000)
        audio_peak = np.max(abs(data))
        seconds_timer += 1

        if audio_peak > 0.06:
            print("<< You (hopefully) caught something! >>\n")
            pyautogui.mouseDown(button='right')
            time.sleep(np.random.uniform(0.03,0.08))
            pyautogui.mouseUp(button='right')
            time.sleep(np.random.uniform(0.35,0.5))
            reeled = True
            break

        if seconds_timer > 12:
            print("<< Failed. Trying again. >>")
            break
 

if __name__ == "__main__":
    print(
        '''
      /`·.¸
     /¸...¸`:·
 ¸.·´  ¸   `·.¸.·´)
: © ):´;      ¸  {
 `·.¸ `·  ¸.·´\`·¸)
     `\\´´\¸.·´
Splash v1.0.                                         
    '''
    )

    global input_device
    global castingkey
    input_device = input("\nSelect your in-game Audio Output device\n[1] Default Speakers [2] VoiceMeeter [3] Exit the app >> ")
    if input_device == '3':
        exit()
    castingkey = input("\nInput your casting key or type exit to quit the program >> ")
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
            time.sleep(np.random.uniform(2.3,3.7))
            print("<< Could not find Bob. Trying again. >>")
            continue





