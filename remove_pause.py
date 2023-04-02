import os


finp = input("File mp4 da cui rimuovere i silezi (senza .mp4):")

stringa = f"py jumpcutter.py --input_file {finp}.mp4 --output_file output_silence.mp4 --sounded_speed 1 --silent_speed 999999 --frame_rate 10"

os.system(stringa)