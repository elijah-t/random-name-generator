import re
import random
import string

def main():

    num = int(input("Enter the number of names you wish to generate: "))

    boyNames = open("boyFirstName.txt", 'r')
    girlNames = open("girlFirstName.txt", 'r')
    surnames = open("surnames.txt", 'r')
    
    boyList = list(map(str.strip, boyNames.readlines()))
    girlList = list(map(str.strip, girlNames.readlines()))
    surnameList = []

    for surname in surnames:
        surnameList.append(re.sub('[^A-Za-z]', '', surname).lower().capitalize().strip())

    for i in range(num):
        if i % 2 == 0:
            print(boyList[random.randint(0, 999)] + " " + random.choice(string.ascii_uppercase) + ". " + surnameList[random.randint(0, 999)])
        else:
            print(girlList[random.randint(0, 999)] + " " + random.choice(string.ascii_uppercase) + ". " + surnameList[random.randint(0, 999)])

main()

