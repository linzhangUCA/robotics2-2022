"""
2. Slowly blink GREEN use PWM (2 seconds gradually on and 2 seconds gradually off). Press B1, GREEN stays on. Press B1 again, GREEN gets back to PWM blinking mode.
3. Count time consumption of GREEN stays on (GO). DO NOT count GREEN blink (GB) time.
4. If GO takes more than 10 seconds, light up YELLOW (other LED will remain their status). 
5. If GO takes more than 20 seconds, blink RED in 2 Hz for 10 seconds. Then, shutdown the system (pull down all involved GPIOs).
6. If press B2 over 3 seconds, turn on BLUE and turn off all other LEDs.
"""

import time
from gpiozero import LED, PWMLED, Button

# instantiate LEDs and buttons
RED = LED(21)
YELLOW = LED(20)
#  blue = LED(12)
green = PWMLED(19, frequency=1000)
plpa = Button(5, hold_time=3)  # B1
rese = Button(6, hold_time=3)  # B2

# set duty cycle for green
duty_cycles = list(range(0, 101)) + list(range(100, -1, -1))  # 0<dc<1
i = 0
FLAG = False
run_time = 0.


try:
    while True:
        # reset mode
        if rese.is_held:
            blue.on()
            time.sleep(3)
            break
        if plpa.is_pressed:
            print("Play/Pause pressed")
            plpa.wait_for_release()
            print("Play/Pause released")
            FLAG = not FLAG
        if FLAG:
            # play mode
            start_time = time.time()
            green.value = 1
            time.sleep(0.02)
            run_time += time.time() - start_time
            if run_time >= 10:
                yellow.on()
            if run_time >= 20:
                for _ in range(20):
                    red.toggle()
                    time.sleep(.5)
                break
        else:
            # pause mode
            green.value = duty_cycles[i] / 100
            time.sleep(0.02)
            i += 1
            if i >= len(duty_cycles):
                i = 0
except KeyboardInterrupt:
    red.off()
    yellow.off()
    blue.off()
    green.off()
    print("\nLEDs are turned off.")
finally:
    red.off()
    yellow.off()
    blue.off()
    green.off()
    print("\nLEDs are turned off.")
