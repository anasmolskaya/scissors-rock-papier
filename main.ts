let Zufall = 0
input.onGesture(Gesture.Shake, function on_gesture_shake() {
    
    Zufall = randint(1, 3)
    if (Zufall == 1) {
        basic.showIcon(IconNames.Scissors)
    } else if (Zufall == 2) {
        basic.showIcon(IconNames.SmallSquare)
    } else {
        basic.showIcon(IconNames.Square)
    }
    
})
