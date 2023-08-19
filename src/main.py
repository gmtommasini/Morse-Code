import sounddevice as sd
import numpy as np
import time
from morse_code_dict import MORSE_CODE_DICT

# Parameters
dot_duration = 0.07  # seconds
dash_duration = dot_duration * 3  # seconds
beep_space = dot_duration
letter_space = dash_duration
word_space = dot_duration * 7

sampling_freq = 44100  # samples per second
frequency = 800  # Hz


def beep(duration):
    sd.play([0.5 * np.sin(2 * np.pi * frequency * t) for t in
             np.linspace(0, duration, int(duration * sampling_freq))], sampling_freq)
    time.sleep(beep_space)


def convert_to_morse_code(text :str):
    output: str = ''
    for char in text.lower():
        if char in MORSE_CODE_DICT:
            code = MORSE_CODE_DICT[char]
            output += code + ' '
            print(code)
            for tap in code:
                if tap == ".":
                    beep(dot_duration)
                elif tap == "-":
                    beep(dash_duration)
                time.sleep(letter_space)
        else:
            time.sleep(letter_space)
    return output


if __name__ == "__main__":
    # text_to_convert = input("Enter the text to convert to Morse code: ")
    text_to_convert = "test morse"
    convert_to_morse_code(text_to_convert)
