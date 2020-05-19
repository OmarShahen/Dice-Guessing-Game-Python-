import random

def checkNumbers(num):
    if num <= 0 or num > 6:
        print("Please enter number from 1 to 6")
        return True
    else:
        return False
def checkGuessing(user,rand):

    if user == rand:
        print("WOW! you guessed it right")
        return
    else:
        result = user - rand
        result = abs(result)
        if result == 5 or result == 4:
            print("Not that close")
        else:
            print("You were close")



print("This is a guessing game for a dice.")

checkResult = True

while(True):
    checkResult = True
    while(checkResult):
        x = input("Enter your Guess: ")
        x = int(x)
        checkResult = checkNumbers(x)

    r = random.randrange(1,7)
    txt = "The Number of the Dice is {}"
    print(txt.format(r))
    checkGuessing(x,r)
    cont = input("Enter 1 to try again and 2 to exit:")
    cont = int(cont)
    if cont == 2:
        print("Hope to see you again BYE!!!")
        break



