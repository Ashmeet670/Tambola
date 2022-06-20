import random


class text:
    yellow = '\033[93m'
    red = '\033[91m'
    darkred = '\033[31m'
    green = '\033[92m'
    cyan = '\033[96m'
    purple = '\033[95m'
    END = '\033[0m'


available_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21,
                     22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40,
                     41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59,
                     60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78,
                     79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90]
choosen_numbers = [0]


def print_board():
    number = 1
    output10 = ""
    output20 = ""
    output30 = ""
    output40 = ""
    output50 = ""
    output60 = ""
    output70 = ""
    output80 = ""
    output90 = ""

    while number < 91:

        if number <= 10:
            if number in available_numbers:
                if number < 10:
                    output10 = output10 + text.purple + \
                        text.yellow + "0" + str(number) + text.purple + "|"
                elif number == 10:
                    output10 = output10 + text.purple + \
                        text.yellow + str(number) + text.purple + "|"

            elif number in choosen_numbers:
                if number < 10:
                    output10 = output10 + text.purple + \
                        text.yellow + str(number) + text.purple + " |"
                elif number == 10:
                    output10 = output10 + text.purple + \
                        text.yellow + str(number) + text.purple + "|"

        elif number <= 20:
            if number in available_numbers:
                output20 = output20 + text.purple + \
                    text.yellow + str(number) + text.purple + "|"

            elif number in choosen_numbers:
                output20 = output20 + text.purple + \
                    text.green + str(number) + text.purple + "|"

        elif number <= 30:
            if number in available_numbers:
                output30 = output30 + text.purple + \
                    text.yellow + str(number) + text.purple + "|"

            elif number in choosen_numbers:
                output30 = output30 + text.purple + \
                    text.green + str(number) + text.purple + "|"

        elif number <= 40:
            if number in available_numbers:
                output40 = output40 + text.purple + \
                    text.yellow + str(number) + text.purple + "|"

            elif number in choosen_numbers:
                output40 = output40 + text.purple + \
                    text.green + str(number) + text.purple + "|"

        elif number <= 50:
            if number in available_numbers:
                output50 = output50 + text.purple + \
                    text.yellow + str(number) + text.purple + "|"

            elif number in choosen_numbers:
                output50 = output50 + text.purple + \
                    text.green + str(number) + text.purple + "|"

        elif number <= 60:
            if number in available_numbers:
                output60 = output60 + text.purple + \
                    text.yellow + str(number) + text.purple + "|"

            elif number in choosen_numbers:
                output60 = output60 + text.purple + \
                    text.green + str(number) + text.purple + "|"

        elif number <= 70:
            if number in available_numbers:
                output70 = output70 + text.purple + \
                    text.yellow + str(number) + text.purple + "|"

            elif number in choosen_numbers:
                output70 = output70 + text.purple + \
                    text.green + str(number) + text.purple + "|"

        elif number <= 80:
            if number in available_numbers:
                output80 = output80 + text.purple + \
                    text.yellow + str(number) + text.purple + "|"

            elif number in choosen_numbers:
                output80 = output80 + text.purple + \
                    text.green + str(number) + text.purple + "|"

        elif number <= 90:
            if number in available_numbers:
                output90 = output90 + text.purple + \
                    text.yellow + str(number) + text.purple + "|"

            elif number in choosen_numbers:
                output90 = output90 + text.purple + \
                    text.green + str(number) + text.purple + "|"

        number += 1

    print(output10)
    print(output20)
    print(output30)
    print(output40)
    print(output50)
    print(output60)
    print(output70)
    print(output80)
    print(output90)


running = True
while running:
    option = input(
        text.purple + "1 for random num / 2 for checking number / 3 for number board " + text.END)
    if option == "1":
        # Making so an invalid number doesn't get choosen
        tempnum = random.choice(available_numbers)
        available_numbers.remove(tempnum)
        choosen_numbers.append(tempnum)

        # Showing the numbers
        tempnum = str(tempnum)
        print(text.yellow + "The number is " + text.cyan + tempnum + text.END)
        tempnum = int(tempnum)

    elif option == "2":
        checknum = int(input(
            text.purple + "Which number to check for? " + text.END))

        numberChosen = False
        for a in choosen_numbers:
            if a == checknum:
                numberChosen = True

        if numberChosen == True:
            print(text.red + "Number already called!" + text.END)
        elif numberChosen == False:
            print(text.green + "Number not called!" + text.END)

    elif option == "3":
        print_board()
