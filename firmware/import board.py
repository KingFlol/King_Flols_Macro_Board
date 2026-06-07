import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation

keyboard = KMKKeyboard()

# Define your matrix pins (adjust to match your wiring)
keyboard.col_pins = (board.D11, board.D10, board.D9)
keyboard.row_pins = (board.D8,)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

# Define what each key does
keyboard.keymap = [
    [KC.A, KC.S, KC.D, KC.W],
]

if __name__ == "__main__":
    keyboard.go()