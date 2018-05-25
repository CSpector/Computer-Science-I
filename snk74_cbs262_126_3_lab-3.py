# Colton Spector and Elias Kossmann
# Lab 3 - Math Quiz
# CS126L-003
# 9/28/2017
from random import randint
import math

runTime = int(input("How many questions would you like?: "))
print("\nWhat would you like the difficulty to be?")
print("Beginner, Intermediate, or Advanced?")
difficulty = input("What do you choose? ").lower()
print("\nPlease follow order of operations when necessary.")
Correct = 0
# Beginner difficulty
if difficulty == 'beginner':
    for i in range(1, int(runTime)+1):
        x = randint(1, 10)
        y = randint(1, 10)
        operand = randint(1, 2)
# Addition problems
        if operand == 1:
            print("\nProblem " + str(i))
            print("%d + %d" % (x, y))
            Answer = int(input("What is the answer? "))
            if Answer == x + y:
                print("You are right.")
                Correct += 1
            else:
                print("You are incorrect.")
# Subtraction Problems
        else:
            print("\nProblem " + str(i))
            print("%d - %d" % (x, y))
            Answer = int(input("What is the answer? "))
            if Answer == x - y:
                print("You are right.")
                Correct += 1
            else:
                print("You are incorrect.")
# Intermediate difficulty
elif difficulty == 'intermediate':
    for i in range(1, int(runTime)+1):
        x = randint(1, 25)
        y = randint(1, 25)
        operand = randint(1, 4)
# Addition Problems
        if operand == 1:
            print("\nProblem " + str(i))
            print("%d + %d" % (x, y))
            Answer = int(input("What is the answer? "))
            if Answer == x + y:
                print("You are right.")
                Correct += 1
            else:
                print("You are incorrect.")
# Subtraction Problems
        elif operand == 2:
            print("\nProblem " + str(i))
            print("%d - %d" % (x, y))
            Answer = int(input("What is the answer? "))
            if Answer == x - y:
                print("You are right.")
                Correct += 1
            else:
                print("You are incorrect.")
# Multiplication Problems
        elif operand == 3:
            print("\nProblem " + str(i))
            print("%d * %d" % (x, y))
            Answer = int(input("What is the answer? "))
            if Answer == x * y:
                print("You are right.")
                Correct += 1
            else:
                print("You are incorrect.")
# Division Problems (Float division)
        else:
            print("\nProblem " + str(i))
            print("%d / %d" % (x, y))
            Answer = input("What is the answer? ")
            Answer = round(float(Answer), 2)
            if Answer == round(x / y, 2):
                print("You are right.")
                Correct += 1
            else:
                print("You are incorrect.")
# Advanced difficulty
else:
    for i in range(1, int(runTime)+1):
        x = randint(1, 10)
        y = randint(1, 10)
        z = randint(1, 10)
        operand1 = randint(1, 4)
        operand2 = randint(1, 4)
# Addition and Addition Problems
        if operand1 == 1:
            if operand2 == 1:
                print("\nProblem " + str(i))
                print("%d + %d + %d" % (x, y, z))
                Answer = int(input("What is the answer? "))
                if Answer == (x + y + z):
                    print("You are correct.")
                    Correct += 1
                else:
                    print("You are incorrect.")
# Addition and Subtraction Problems
            if operand2 == 2:
                print("\nProblem " + str(i))
                print("%d + %d - %d" % (x, y, z))
                Answer = int(input("What is the answer? "))
                if Answer == (x + y - z):
                    print("You are correct.")
                    Correct += 1
                else:
                    print("You are incorrect.")
# Addition and Multiplication Problems
            if operand2 == 3:
                print("\nProblem " + str(i))
                print("%d + %d * %d" % (x, y, z))
                Answer = int(input("What is the answer? "))
                if Answer == (x + y * z):
                    print("You are correct.")
                    Correct += 1
                else:
                    print("You are incorrect.")
# Addition and Division Problems (Float Division)
            if operand2 == 4:
                print("\nProblem " + str(i))
                print("%d + %d / %d" % (x, y, z))
                Answer = round(float(input("What is the answer? ")), 2)
                if Answer == (x + y / z):
                    print("You are correct.")
                    Correct += 1
                else:
                    print("You are incorrect.")
# Subtraction and Addition Problems
        elif operand1 == 2:
            if operand2 == 1:
                print("\nProblem " + str(i))
                print("%d - %d + %d" % (x, y, z))
                Answer = int(input("What is the answer? "))
                if Answer == (x-y+z):
                    print("You are correct.")
                    Correct += 1
                else:
                    print("You are incorrect.")
# Subtraction and Subtraction Problems
            if operand2 == 2:
                print("\nProblem " + str(i))
                print("%d - %d - %d" % (x, y, z))
                Answer = int(input("What is the answer? "))
                if Answer == (x - y - z):
                    print("You are correct.")
                    Correct += 1
                else:
                    print("You are incorrect.")
# Subtraction and Multiplication Problems
            if operand2 == 3:
                print("\nProblem " + str(i))
                print("%d - %d * %d" % (x, y, z))
                Answer = int(input("What is the answer? "))
                if Answer == (x - y * z):
                    print("You are correct.")
                    Correct += 1
                else:
                    print("You are incorrect.")
# Subtraction and Division Problems (Float Division)
            if operand2 == 4:
                print("\nProblem " + str(i))
                print("%d - %d / %d" % (x, y, z))
                Answer = round(float(input("What is the answer? ")), 2)
                if Answer == round((x - y/z), 2):
                    print("You are correct.")
                    Correct += 1
                else:
                    print("You are incorrect.")
# Multiplication and Addition Problems
        elif operand1 == 3:
            if operand2 == 1:
                print("\nProblem " + str(i))
                print("%d * %d + %d" % (x, y, z))
                Answer = int(input("What is the answer? "))
                if Answer == (x * y + z):
                    print("You are correct.")
                    Correct += 1
                else:
                    print("You are incorrect.")
# Multiplication and Subtraction Problems
            if operand2 == 2:
                print("\nProblem " + str(i))
                print("%d * %d - %d" % (x, y, z))
                Answer = int(input("What is the answer? "))
                if Answer == (x * y - z):
                    print("You are correct.")
                    Correct += 1
                else:
                    print("You are incorrect.")
# Multiplication and Multiplication Problems
            if operand2 == 3:
                print("\nProblem " + str(i))
                print("%d * %d * %d" % (x, y, z))
                Answer = int(input("What is the answer? "))
                if Answer == (x * y * z):
                    print("You are correct.")
                    Correct += 1
                else:
                    print("You are incorrect.")
# Multiplication and Division Problems (Float Division)
            if operand2 == 4:
                print("\nProblem " + str(i))
                print("%d * %d / %d" % (x, y, z))
                Answer = round(float(input("What is the answer? ")), 2)
                if Answer == round((x * y/z), 2):
                    print("You are correct.")
                    Correct += 1
                else:
                    print("You are incorrect.")
        else:
            if operand2 == 1:
                print("\nProblem " + str(i))
                print("%d / %d + %d" % (x, y, z))
                Answer = round(float(input("What is the answer? ")), 2)
                if Answer == round((x/y + z), 2):
                    print("You are correct.")
                    Correct += 1
                else:
                    print("You are incorrect.")
# Division and Subraction Problems (Float Division)
            if operand2 == 2:
                print("\nProblem " + str(i))
                print("%d / %d - %d" % (x, y, z))
                Answer = round(float(input("What is the answer? ")), 2)
                if Answer == round((x/y - z), 2):
                    print("You are correct.")
                    Correct += 1
                else:
                    print("You are incorrect.")
# Division and Multiplication Problems (Float Division)
            if operand2 == 3:
                print("\nProblem " + str(i))
                print("%d / %d * %d" % (x, y, z))
                Answer = round(float(input("What is the answer? ")), 2)
                if Answer == round((x/y * z), 2):
                    print("You are correct.")
                    Correct += 1
                else:
                    print("You are incorrect.")
# Division and Division Problems (Float Division)
            if operand2 == 4:
                print("\nProblem " + str(i))
                print("%d / %d / %d" % (x, y, z))
                Answer = round(float(input("What is the answer? ")), 2)
                if Answer == round((x/y/z), 2):
                    print("You are correct.")
                    Correct += 1
                else:
                    print("You are incorrect.")
if Correct > (runTime*(2/3)):
    print("\nWell done!")
elif Correct <= (runTime*(2/3)) and Correct > (runTime*(1/3)):
    print("\nYou need more practice.")
else:
    print("\nPlease ask your math teacher for help!")
