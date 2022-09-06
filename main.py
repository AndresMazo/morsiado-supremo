def add_point():
    global values
    values = "" + values + "."
def get_word(text: str):
    global words
    if text == ".-":
        words = "" + words + "a"
    elif text == "-...":
        words = "" + words + "b"
    elif text == "-.-.":
        words = "" + words + "c"
    elif text == "-..":
        words = "" + words + "d"
    elif text == ".":
        words = "" + words + "e"
    elif text == "..-.":
        words = "" + words + "f"
    elif text == "--.":
        words = "" + words + "g"
    elif text == "....":
        words = "" + words + "h"
    elif text == "..":
        words = "" + words + "i"
    elif text == ".---":
        words = "" + words + "j"
    elif text == "-.-":
        words = "" + words + "k"
    elif text == ".-..":
        words = "" + words + "l"
    elif text == "--":
        words = "" + words + "m"
    elif text == "-.":
        words = "" + words + "n"
    elif text == "---":
        words = "" + words + "o"
    elif text == ".--.":
        words = "" + words + "p"
    elif text == "--.-":
        words = "" + words + "q"
    elif text == ".-.":
        words = "" + words + "r"
    elif text == "...":
        words = "" + words + "s"
    elif text == "-":
        words = "" + words + "t"
    elif text == "..-":
        words = "" + words + "u"
    elif text == "...-":
        words = "" + words + "v"
    elif text == ".--":
        words = "" + words + "w"
    elif text == "-..-":
        words = "" + words + "x"
    elif text == "-.--":
        words = "" + words + "y"
    elif text == "--..":
        words = "" + words + "z"
    elif text == "/":
        words = "" + words + " "
    elif text == "-----":
        words = "" + words + "0"
    elif text == ".----":
        words = "" + words + "1"
    elif text == "..---":
        words = "" + words + "2"
    elif text == "...--":
        words = "" + words + "3"
    elif text == "....-":
        words = "" + words + "4"
    elif text == ".....":
        words = "" + words + "5"
    elif text == "-....":
        words = "" + words + "6"
    elif text == "--...":
        words = "" + words + "7"
    elif text == "---..":
        words = "" + words + "8"
    elif text == "----.":
        words = "" + words + "9"
    else:
        restar()
        basic.show_string("E:")
        basic.show_string(text)
def add_stripe():
    global values
    values = "" + values + "-"
def add_next_word():
    global values
    values = "" + values + "/"
def restar():
    global values, words, morse_letter, i
    values = ""
    words = ""
    morse_letter = ""
    i = 0
    basic.show_leds("""
        . . . . .
                . . . . .
                . . . . .
                . . . . .
                . . . . .
    """)
def traslete():
    global c, values_old, index_end, morse_letter, i
    c = len(values.split(" "))
    values_old = values
    while i < c and values and len(values) > 0:
        if values_old.index_of(" ") >= 1:
            index_end = values_old.index_of(" ")
        else:
            index_end = len(values_old)
        morse_letter = values_old.substr(0, index_end)
        get_word(morse_letter)
        values_old = values_old.substr(index_end + 1, len(values_old))
        i += 1
    basic.show_string(words)
    restar()

def on_received_number_deprecated(receivedNumber):
    if receivedNumber == 0:
        add_point()
        basic.show_leds("""
            . . . . .
                        . # # # .
                        . # # # .
                        . # # # .
                        . . . . .
        """)
    elif receivedNumber == 1:
        add_stripe()
        basic.show_leds("""
            . . . . .
                        . . . . .
                        . # # # .
                        . . . . .
                        . . . . .
        """)
    elif receivedNumber == 2:
        add_space()
        basic.show_leds("""
            . . # . .
                        . . . # .
                        # # # # #
                        . . . # .
                        . . # . .
        """)
    elif receivedNumber == 3:
        add_space()
        add_next_word()
        add_space()
        basic.show_leds("""
            . . . . #
                        . . . # .
                        . . # . .
                        . # . . .
                        # . . . .
        """)
    elif receivedNumber == 4:
        restar()
    basic.pause(100)
    basic.show_leds("""
        . . . . .
                . . . . .
                . . . . .
                . . . . .
                . . . . .
    """)
radio.on_received_number_deprecated(on_received_number_deprecated)

def on_button_pressed_a():
    basic.show_leds("""
        . . . . .
                . # # # .
                . # # # .
                . # # # .
                . . . . .
    """)
    radio.send_number(0)
    basic.pause(100)
    basic.show_leds("""
        . . . . .
                . . . . .
                . . . . .
                . . . . .
                . . . . .
    """)
input.on_button_pressed(Button.A, on_button_pressed_a)

def add_space():
    global values
    values = "" + values + " "

def on_button_pressed_ab():
    basic.show_leds("""
        . . # . .
                . . . # .
                # # # # #
                . . . # .
                . . # . .
    """)
    radio.send_number(2)
    basic.pause(100)
    basic.show_leds("""
        . . . . .
                . . . . .
                . . . . .
                . . . . .
                . . . . .
    """)
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    basic.show_leds("""
        . . . . .
                . . . . .
                . # # # .
                . . . . .
                . . . . .
    """)
    radio.send_number(1)
    basic.pause(100)
    basic.show_leds("""
        . . . . .
                . . . . .
                . . . . .
                . . . . .
                . . . . .
    """)
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_gesture_shake():
    traslete()
    radio.send_number(4)
    basic.pause(100)
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

def on_logo_pressed():
    basic.show_leds("""
        . . . . #
                . . . # .
                . . # . .
                . # . . .
                # . . . .
    """)
    radio.send_number(3)
    basic.pause(100)
    basic.show_leds("""
        . . . . .
                . . . . .
                . . . . .
                . . . . .
                . . . . .
    """)
input.on_logo_event(TouchButtonEvent.PRESSED, on_logo_pressed)

index_end = 0
values_old = ""
c = 0
i = 0
values = ""
morse_letter = ""
words = ""
words = ""
morse_letter = ""
radio.set_transmit_power(7)
radio.set_group(1)