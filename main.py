Zufall = 0

def on_gesture_shake():
    global Zufall
    Zufall = randint(1, 3)
    if Zufall == 1:
        basic.show_icon(IconNames.SCISSORS)
    elif Zufall == 2:
        basic.show_icon(IconNames.SMALL_SQUARE)
    else:
        basic.show_icon(IconNames.SQUARE)
input.on_gesture(Gesture.SHAKE, on_gesture_shake)
