#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
E-G with a simple menu to start up with.
E-G didn't do anything, just present a menu with some choices.
You should add functinoality E-G.

"""


def meImage():
    """
    Store my ascii image in a separat variabel as a raw string
    """
    return r"""


                                  \\|//
                             _.-~~~~~~~~~-._
             ___.----._    /~               ~\
          .-~          ~\/'                   `\
        /~              ;                       \
       ;               ;
      (               ;                           ;
     (                |                |          |
     )                |         |      |          |
    (   /\   |     /  |         |       \     |   '
    )   | \_  \   ,,;':   |\     \ , ', ,,   /   ;
   (    |   ~-.` `     |  | `\` ``'       ' ',, ;
   )    |           |\  |/                      ~\
   (   _|  /|       (_)(~|  /|        |\         |
   )  ( | (_)  .--.     \: (_)   __   (_)      _/
   (   `\\               `;     '  `         /~
   \     `\_   .___.   _/' \               .'
    (       ~-.___...-~     `-._.    . _.-~
     )        /(____/~/@~\   /~\~`--~)\
     (      /@`--..--'   @\(' / |~~~'\ |\
      (__.-< )       ) @   )  |_|    |_||
           /@|      (@    /   (_)-..-(_)`\
          (  \      \_  @|    `)       <  |
          >  @)   __/ @  \    /\_     , ~\
         /@  _> (~ ~\   @|/\     ~\_/''/) )
         \_@/ /~~\@       \/       ||   )'
     _.-~  \ (/   )_ @_.-'/~\_   _/-'~-~  `\
   /~       ~`-'~~  ~~/  /    ~~~     //\   )
  |     /          _.'  ,|            \/"|  |
  |    /         /~__.-~  \_              \ |
  ~-._|        _/ /  ~----~ ~-.__         )  \
   /  /~-.__./~  `)     |        ~~(      \  |
  '~-|_          < |    |   |      |       > |
     _-~--.__   _/'     |         <        |-'
    (  ,-\\  ~~)       ;\.    |   |  __.--~-.|
    `~(____.--~  |    ;   `.    | `~~(___ '''~)
          /  |       ;      \           \~~~/~

"""

def meny():
    """menyn på mat"""
    return r"""
            | Namn         | Pris|
    --------|--------------|-----|
    Rätter  |1. kebab      | 150 |
    --------|tallrik       |     |
            |--------------|-----|
            |2. kyckling   | 150 |
            |tallrik       |     |
            |--------------|-----|
            |3. hambugare  | 150 |
            |tallrik       |     |
    --------|--------------|-----|
    Dricka  |1. Cola       | 50  |
            |2. sprite     | 50  |
            |3. fanta      | 50  |
            |4. kaffe      | 25  |
            |5. te         | 20  |
            |6  vatten     | 20  |
   -------------------------------
    """



def menu():
    """
    Display the menu with the options that E-G can do.
    """
    print(chr(27) + "[2J" + chr(27) + "[;H")
    print(meImage())
    print("Hi, We are E-G. We know it all. What can we do for you?")
    print("1) Present yourself to E-G.")
    print("2) Convert year(s) to second(s).")
    print("3) If you want to know your weight on the moon.")
    print("4) Convert minute(s) to hour(s).")
    print("5) Convert celsius into fahrenheit.")
    print("6) If you want to multiply a sentence")
    print("7) jumble of numbers (max and min).")
    print("8) If you want to addition and know the main value")
    print("9) To calculate the circle's area")
    print("10) To calculate the triangle's hypotenuse")
    print("11) If you want to know you grade report.")
    print("12) Guess the number.")
    print("13) What time is it?")
    print("14) Kasta om bokstäver!")
    print("15) Säg HEJ till E-G,fråga om en citat elle luchställe")
    print("16) If you want E-G analyse a fil for you?")
    print("q) Quit.")

def myNameIs():
    """
    Read the users name and say hello.
    """
    print("My presentation")
    print("---------------")
    print("Our name's E-G")
    name = input("What is your name? ")
    print("\nE-G say:\n")
    print("Hello %s - your awesomeness!\n" % name)


def old():
    """
    read the users age
    """
    print("How to convert year to seconds")
    print("------------------------------")
    age = input("How old are you? : ")
    age = int(age)
    if age > 0:
        b = age*31557600
        print("\nE-G say:\n")
        print("Great! your are %s years old" % age)
        print("It means you have lived %s secondes" % b)
        return
    else:
        return "Wrong answer i suppose"


def tingd():
    """
    vikten på månen
    """
    print("I left half a ton Leg-press on the moon")
    print("---------------------------------------")
    vikt = input("how much do you weight? : ")
    vikt = int(vikt)
    c = vikt/6
    print("\nE-G say:\n")
    print("Nice! your weight is %s Kg" % vikt)
    print("Do you know that you weight just %s Kg on the moon" % c)
    return

def minute():
    """
    konvertera minuter till timmar
    """
    print("How to convert minute(s) to hour(s)")
    print("---------------------------------")
    minuterOne = input("How long should you brush your teeth for? (min): ")
    minuterTwo = input("How long should you wash your body for? (min): ")
    minuterThree = input("And how long is your travel to the school? (min): ")
    minuterOne = int(minuterOne)
    minuterTwo = int(minuterTwo)
    minuterThree = int(minuterThree)
    minuterTotal = minuterOne+minuterTwo+minuterThree
    timmar = 0

    while (minuterTotal >= 60):
        minuterTotal = minuterTotal-60
        timmar = timmar+1

    print("\nE-G say:\n")
    print("You take in all %s hour(s)" % timmar)
    print("and %s minutes in the morning" % minuterTotal)


def weather():
    """
    konvertera celsius till F
    """
    print("How to convert celsius into fahrenheit")
    print("--------------------------------------")
    celsius = input("How's the weather today? How many degrees celsius? : ")
    celsius = int(celsius)
    e = celsius*9/5+32
    print("\nE-G say:\n")
    print("%s degrees celsius =" % celsius)
    print("%s fahrenheit" % e)
    return

def word():
    """
    ord-loopen
    """
    print("Multiply a word")
    print("---------------")
    ordet = input("Enter a word of your choise : ")
    lop = input("How many times dou you want E-G to repeat the word? : ")
    lop = int(lop)
    x = 0

    while (x < lop):
        x = x+1
        print(x, ordet)

def slumpmassiga():
    """
    välja ett slumpmässiga tal mellan max och min
    """
    print("Random jumble of numbers")
    print("------------------------")
    maxim = input("Enter a maximum value on an interval : ")
    maxim = int(maxim)
    minim = input("Enter the minumun value : ")
    minim = int(minim)
    z = 0
    for i in range(minim, maxim, 3):
        print(i, end=', ')
        z = z+1
        if z == 10:
            break
        else:
            continue

def summaMedel():
    """
    summa ut och räkna medel
    """
    summan = 0
    medel = 0
    antalVardern = 0
    talet = 0
    print("Addition and Mean value")
    print("------------------------")

    while str(talet) != str("done"):
        talet = input("choice a number or enter 'done' if you finish : ")
        if talet == "done":
            break
        else:
            antalVardern = antalVardern + 1
            talet = int(talet)
            summan = summan+talet
            medel = summan/antalVardern

    print("\nE-G say:\n")
    print("Total = %s " % summan)
    print("Mean value = %s " % medel)

def cirkel():
    """
    Räknar ut arean av cirkel
    """
    print("circle area enclosed")
    print("--------------------")
    radian = input("Enter the circle's radius(cm) : ")
    radian = int(radian)
    import math
    arean = math.pi*radian*radian
    print("\nE-G say:\n")
    print("Area = %s cm^2" % arean)

def hypotenuse():
    """
    räknar ut hypotenusa
    """
    print("Pythagorean theorem")
    print("-----------------------")
    rightAngleA = input("Enter the first leg a (cm) : ")
    rightAngleA = int(rightAngleA)
    rightAngleB = input("Enter the second leg b (cm) : ")
    rightAngleB = int(rightAngleB)
    import math
    hypotenusa = math.sqrt(rightAngleA*rightAngleA)+(rightAngleB*rightAngleB)
    print("\nE-G say:\n")
    print("hypotenuse = %s cm" % hypotenusa)


def betyg():
    """
    Betyg
    """
    maxPoing = float(input("How many points was max?"))
    yourPoints = float(input("How many points did you get?"))
    if yourPoints > maxPoing * 1:
        print("something is wrong!")
    elif yourPoints >= maxPoing * 0.9:
        print("Betyg: A")
    elif yourPoints >= maxPoing * 0.8:
        print("Betyg: B")
    elif yourPoints >= maxPoing * 0.7:
        print("Betyg: C")
    elif yourPoints >= maxPoing * 0.6:
        print("Betyg: D")
    elif yourPoints < maxPoing * 0.6:
        print("betyg: F")
    else:
        print("something is wrong")


def guessa():
    """Guess the number"""
    import random
    guessTime = 0

    print('Hello! This is a <Guess the number> game')
    print('I am thinking of a number between 1 and 100 and you will try to find which the numerber is.')
    print('You are just six chances')

    myName = input("What is your name? : ")
    number = random.randint(1, 100)
    print('Well,' + myName + ', choose any number between 1 and 100 : ')

    while guessTime < 6:
        print('Take a guess : ')
        guess = input()
        guess = int(guess)
        guessTime = guessTime + 1

        if guess < number:
            print('Your guess is too low.')
        if guess > number:
            print('Your guess is too high.')
        if guess == number:
            break

    if guess == number:
        guessTime = str(guessTime)
        print('Well done, ' + myName + '! you did that in '+ guessTime + ' guesses!')
    if guess != number:
        number = str(number)
        print('sorry you had just six chanses and the number i was thinking of was '+number)

def timeNow():
    """actually time and humör"""
    import random
    import time

    fhand = open("format.txt")
    line = fhand.readline()
    locatime = time.asctime(time.localtime(time.time()))

    moods = ["happy", "sad", "depressed", "angry", "annoyed", "bored", "confused", "excited", "lonely"]
    mood = random.choice(moods)

    smilies = [":)", ":(", ":D", ":/", ":|", ":'(", ":O", ":@", ":P", ":3"]
    smiley = random.choice(smilies)

    heltal = 10
    floatal = round(2.475, 3)


    print(line.format(locatime=locatime, mood=mood, smiley=smiley, heltal=heltal, floatal=floatal))

def kasta():
    """change letter's position"""
    import random

    """words = input("writte one word of your choice? : ")
    sl = list(words)
    random.shuffle(sl)

    print("".join(sl))"""

    words = input("writte one word of your choice? : ")
    new_words = random.sample(words, len(words))
    print('E-G says : '+ "".join(new_words))


def ask():
    """E-G svarar på löpande text"""
    import random

    lunchQuote = ['ska vi ta en kaffe?', 'ska vi dra ned till bistro?',
                  'jag tänkte käka på macdonals, ska du med?',
                  'På Wallys är det mysigt, ska vi ta där?']

    hello = ['Hej själv! ', 'Trevligt att du bryr dig om mig. ',
             'Det var länge sedan någon var trevlig mot mig. ',
             'Halloj, det ser ut att bli mulet idag.']

    smilies = [":)", ":(", ":D", ":/", ":|", ":'(", ":O", ":@", ":P", ":3"]

    print("Hello i'm E-G, what can i do for you?")



    while True:
        question = input("Enter your question or 'done' to quit : ")
        with open('quotes.txt', 'r') as line:
            data = line.read().replace('\n', '')
            listeQuotes = data.split('.')
            listeQuotesRemix = random.choice(listeQuotes)
            greatning = random.choice(hello)
            smiley = random.choice(smilies)
            mesages = random.choice(lunchQuote)
        if question == 'done':
            break

        elif "citat" in question.lower() or 'citation' in question.lower():
            print("What do you say about this quote : ")
            print('\"'+listeQuotesRemix+ '\"'+smiley)

        elif "lunch" in question.lower():
            print(mesages)
            reponse = input()

            if reponse.lower() == 'nej':
                print('vad synd! nästa gång då'+smiley)

            elif reponse.lower() == 'ja' or reponse.lower() == 'yes' or reponse.lower() == 'japp':
                print('Bra! så här ser menyn : ')
                print(meny())

            else:
                print('svara med ja eller nej')


        elif 'hej' in question.lower() or 'hello' in question.lower():
            print(greatning + smiley)

        else:
            print('i dont understand')
