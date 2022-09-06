function add_point () {
    values = "" + values + "."
}
function get_word (text: string) {
    if (text == ".-") {
        words = "" + words + "a"
        console.log("++++++")
    } else if (text == "-...") {
        words = "" + words + "b"
    } else if (text == "-.-.") {
        words = "" + words + "c"
    } else if (text == "-..") {
        words = "" + words + "d"
    } else if (text == ".") {
        words = "" + words + "e"
    } else if (text == "..-.") {
        words = "" + words + "f"
    } else if (text == "--.") {
        words = "" + words + "g"
    } else if (text == "....") {
        words = "" + words + "h"
    } else if (text == "..") {
        words = "" + words + "i"
    } else if (text == ".---") {
        words = "" + words + "j"
    } else if (text == "-.-") {
        words = "" + words + "k"
    } else if (text == ".-..") {
        words = "" + words + "l"
    } else if (text == "--") {
        words = "" + words + "m"
    } else if (text == "-.") {
        words = "" + words + "n"
    } else if (text == "---") {
        words = "" + words + "o"
    } else if (text == ".--.") {
        words = "" + words + "p"
    } else if (text == "--.-") {
        words = "" + words + "q"
    } else if (text == ".-.") {
        words = "" + words + "r"
    } else if (text == "...") {
        words = "" + words + "s"
    } else if (text == "-") {
        words = "" + words + "t"
    } else if (text == "..-") {
        words = "" + words + "u"
    } else if (text == "...-") {
        words = "" + words + "v"
    } else if (text == ".--") {
        words = "" + words + "w"
    } else if (text == "-..-") {
        words = "" + words + "x"
    } else if (text == "-.--") {
        words = "" + words + "y"
    } else if (text == "--..") {
        words = "" + words + "z"
    } else if (text == "/") {
        words = "" + words + " "
    } else if (text == "-----") {
        words = "" + words + "0"
    } else if (text == ".----") {
        words = "" + words + "1"
    } else if (text == "..---") {
        words = "" + words + "2"
    } else if (text == "...--") {
        words = "" + words + "3"
    } else if (text == "....-") {
        words = "" + words + "4"
    } else if (text == ".....") {
        words = "" + words + "5"
    } else if (text == "-....") {
        words = "" + words + "6"
    } else if (text == "--...") {
        words = "" + words + "7"
    } else if (text == "---..") {
        words = "" + words + "8"
    } else if (text == "----.") {
        words = "" + words + "9"
    } else {
        restar()
        console.log("Error")
basic.showString("E:")
        basic.showString(text)
    }
}
function add_stripe () {
    values = "" + values + "-"
}
function add_next_word () {
    values = "" + values + "/"
}
function restar () {
    values = ""
    words = ""
    morse_letter = ""
    i = 0
    basic.showLeds(`
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        `)
}
function traslete () {
    // c =  values.split(' ').length;
    c = values.split(" ").length
    values_old = values
    while (i < c && values && values.length > 0) {
        if (values_old.indexOf(" ") >= 1) {
            index_end = values_old.indexOf(" ")
        } else {
            index_end = values_old.length
        }
        morse_letter = values_old.substr(0, index_end)
        // get_word(morse_letter)
        get_word(".-")
        values_old = values_old.substr(index_end + 1, values_old.length)
        i += 1
    }
    basic.showString(words)
    restar()
}
radio.onReceivedNumberDeprecated(function (receivedNumber) {
    if (receivedNumber == 0) {
        add_point()
        basic.showLeds(`
            . . . . .
            . . . . .
            . . # . .
            . . . . .
            . . . . .
            `)
    } else if (receivedNumber == 1) {
        add_stripe()
        basic.showLeds(`
            . . . . .
            . . . . .
            . # # # .
            . . . . .
            . . . . .
            `)
    } else if (receivedNumber == 2) {
        add_space()
        basic.showLeds(`
            . . . . .
            . . . # .
            . . # . .
            . # . . .
            . . . . .
            `)
    } else if (receivedNumber == 3) {
        add_space()
        add_next_word()
        add_space()
        basic.showLeds(`
            . # # # .
            # . . # #
            # # # # #
            . # # # #
            . # . # .
            `)
    } else if (receivedNumber == 4) {
        restar()
    }
    basic.pause(100)
    basic.clearScreen()
})
input.onButtonPressed(Button.A, function () {
    basic.showLeds(`
        . . . . .
        . . . . .
        . . # . .
        . . . . .
        . . . . .
        `)
    radio.sendNumber(0)
    basic.pause(100)
    basic.clearScreen()
})
function add_space () {
    values = "" + values + " "
}
input.onButtonPressed(Button.AB, function () {
    basic.showLeds(`
        . . . . .
        . . . # .
        . . # . .
        . # . . .
        . . . . .
        `)
    radio.sendNumber(2)
    basic.pause(100)
    basic.clearScreen()
})
input.onButtonPressed(Button.B, function () {
    basic.showLeds(`
        . . . . .
        . . . . .
        . # # # .
        . . . . .
        . . . . .
        `)
    radio.sendNumber(1)
    basic.pause(100)
    basic.clearScreen()
})
input.onGesture(Gesture.Shake, function () {
    traslete()
    radio.sendNumber(4)
    basic.pause(100)
})
input.onLogoEvent(TouchButtonEvent.Pressed, function () {
    basic.showLeds(`
        . # # # .
        # . . # #
        # # # # #
        . # # # #
        . # . # .
        `)
    radio.sendNumber(3)
    basic.pause(100)
    basic.clearScreen()
})
let index_end = 0
let values_old = ""
let c = 0
let i = 0
let values = ""
let morse_letter = ""
let words = ""
words = ""
morse_letter = ""
radio.setTransmitPower(7)
radio.setGroup(1)
