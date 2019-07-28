import time
from colorzero import Color
from espeak import espeak
from sense_hat import SenseHat

sense = SenseHat()
sense.low_light = True
espeak.set_voice("en-us+f2")
color = ""

espeak.synth("Enter the color")
while espeak.is_playing():
    time.sleep(0.5)
    
while color != "e":    
    color = input("Enter the color (enter \"e\" to exit): ")
    color = color.lower()
    if color != "e":
        try:                 
            sense.clear(Color(color).rgb_bytes)
            espeak.synth("Here is " + color)
            while espeak.is_playing():
                time.sleep(0.5)
        except:
            msg = color + ' is not a valid color. Try again!'
            print(msg)
            espeak.synth(msg)
            while espeak.is_playing():
                time.sleep(0.5)
    else:
        espeak.synth("Good bye!")
        sense.clear(Color("black").rgb_bytes)

