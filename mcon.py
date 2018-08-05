from time import sleep
import RPi.GPIO as IO

IO.setmode(IO.BCM)
IO.setwarnings(0)
IO.setup(26, IO.OUT)

dash = 3
dot = 1
word = 7
mult = 0.5

mtable = (".-",  # A
          "-...",  # B
          "-.-.",  # C
          "-..",  # D
          ".",  # E
          "..-.",  # F
          "--.",  # G
          "....",  # H
          "..",  # I
          ".---",  # J
          "-.-",  # K
          ".-..",  # L
          "--",  # M
          "-.",  # N
          "---",  # O
          ".--.",  # P
          "--.-",  # Q
          ".-.",  # R
          "...",  # S
          "-",  # T
          "..-",  # U
          "...-",  # V
          ".--",  # W
          "-..-",  # X
          "-.--",  # Y
          "--..",  # Z
          ".----",  # 1
          "..---",  # 2
          "...--",  # 3
          "....-",  # 4
          ".....",  # 5
          "-....",  # 6
          "--...",  # 7
          "---..",  # 8
          "----.",  # 9
          "-----")  # 0

mtrans = ("A",  # A
          "B",  # B
          "C",  # C
          "D",  # D
          "E",  # E
          "F",  # F
          "G",  # G
          "H",  # H
          "I",  # I
          "J",  # J
          "K",  # K
          "L",  # L
          "M",  # M
          "N",  # N
          "O",  # O
          "P",  # P
          "Q",  # Q
          "R",  # R
          "S",  # S
          "T",  # T
          "U",  # U
          "V",  # V
          "W",  # W
          "X",  # X
          "Y",  # Y
          "Z",  # Z
          "1",  # 1
          "2",  # 2
          "3",  # 3
          "4",  # 4
          "5",  # 5
          "6",  # 6
          "7",  # 7
          "8",  # 8
          "9",  # 9
          "0")  # 0


def mcon(string):
    global mtable
    global mtrans
    global dot
    global dash
    global mult
    global word

    string = string.upper()

    morse = []

    chars = list(string)

    for i in chars:
        if i in mtrans:
            k = mtrans.index(i)
            morse.append(mtable[k])
        else:
            morse.append(" ")

    for x in morse:
        if x == " ":
            sleep(mult * word)

        elif x != " ":
            morsechar = list(x)

            for m in morsechar:
                if m == ".":
                    doadot()

                elif m == "-":
                    dotadash()

                sleep(mult * dot)


def doadot():
    global dot
    global mult

    IO.output(26, 1)
    sleep(mult * dot)
    IO.output(26, 0)


def dotadash():
    global dash
    global mult

    IO.output(26, 1)
    sleep(mult * dash)
    IO.output(26, 0)


mcon("a b")  # put text to convert in here.
