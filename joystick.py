import pygame

# BUTTON CODES
#
# L = 4
# R = 5
#
# X 0
# Y 3
# A 1
# B 2
#
# Start 8
# Select 9
#

BUTTONS_VALUES = {
    "L": 4,
    "R": 5,
    "X": 0,
    "Y": 3,
    "A": 1,
    "B": 2,
    "START": 9,
    "SELECT": 8,
    "LEFT": (0, -1),
    "RIGHT": (0, 1),
    "UP": (1, -1),
    "DOWN": (1, 1)
}

class PygameCustomJoystick:
    def __init__(self, joystick=None) -> None:
        self.joystick = joystick
    
    def clicked(self, button, event):
        button = button.upper()
        
        if not button in BUTTONS_VALUES.keys():
            raise KeyError("Not valid button type")

        if "joy" in dir(event):
            if self.joystick != None and (event.joy != self.joystick.get_id()):
                return False
            else:
                btnVal = BUTTONS_VALUES[button]
                if isinstance(btnVal, tuple) and event.type == pygame.JOYAXISMOTION:
                    return (round(event.axis) == btnVal[0] and round(event.value) == btnVal[1])
                elif isinstance(btnVal, int) and event.type == pygame.JOYBUTTONDOWN:
                    return event.button == btnVal
                
        return False
                