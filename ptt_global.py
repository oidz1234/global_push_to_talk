from pynput.keyboard import Key, Listener
import subprocess

#ptt = 'p'
ptt = Key.caps_lock

def unmute():
    # logic here to check if we have already unmuted mic
    # amixer sget Capture | grep  '\[on\]' <- check if mic is on
    # amixer sset Capture cap
    cmd = 'amixer sget Capture | grep -F [on]'
    # bad
    result = subprocess.run(cmd, shell=True)
    if result.returncode == 1:
        print('we will unmute microphone')
        subprocess.run(["amixer", "sset", "Capture", "cap"])
    else:
        print('we will not unmute because we are already unmuted!')


def mute():
    # amixer sset Capture nocap
    subprocess.run(["amixer", "sset", "Capture", "nocap"])

    print('we will mute microphone')

def on_press(key):
    print(key)
    print(ptt)
    # almost 100% sure there is a way to do this better
    try:
        if key.char == ptt:
            unmute()
    except AttributeError:
        if key == ptt:
            unmute()
        print('caught key that is not a char')

def on_release(key):
    print(key)
    print(ptt)
    # almost 100% sure there is a way to do this better
    try:
        if key.char == ptt:
            mute()
    except AttributeError:
        if key == ptt:
            mute()
        print('caught key that is not a char')

    if key == Key.esc:
        # Stop listener
        return False

# Collect events until released
with Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()
