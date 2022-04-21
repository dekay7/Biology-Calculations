import math
from fractions import *

# Define Calculations
# Population Growth (Exponential)
def epopg(r=None, N=None, t=None):
    while True:    
        if (r == None) and (N == None) and (t == None):
            r = Fraction(input("enter the per capita growth rate: \n"))
            N = Fraction(input("enter the initial population size: \n"))
            t = Fraction(input("enter the difference in time (dt): \n"))
            break
        else:
            break
    newpop = float(N * (math.pow(1+r, t)))
    return newpop

# Population Growth (Logarithmic)
def lpopg(r=None, N=None, t=None, K=None):
    exit()

# Chi-Square
def chisq():
    observed = []
    expected = []
    print("enter observed values: ")
    while True:
        while True:
            value = input()
            if value != 's':
                observed.append(Fraction(value))
                continue
            else:
                break
        print("enter expected values: ")
        while True:
            value = input()
            if value != 's':
                expected.append(Fraction(value))
                continue
            else:
                break
        if len(observed) == len(expected):
            break
        else: 
            print("re-enter data, respectively... ")
            continue
    oediffsqd = []
    oblength = len(observed)
    for i in range(oblength):
        oediff = float(observed[i] - (expected[i]))
        oediffsqd.append(float((math.pow(oediff, 2))/(expected[i])))
    chiSq = sum(oediffsqd)
    return chiSq

# Simpson's Diversity Index
def sdi():
    

while True:
    action = str(input("which calculation? \n"))

# On Exit
    if action == 'exit':
        break

# Population Growth
    elif action == 'popg':
        option = input("exponential 'e' or logarithmic 'l'? \n")
        while True:
            if option == 'e':
                newpop = epopg()
                break
            elif option == 'l':
                newpop = lpopg()
                break
            else: 
                print("choose either exponential 'e' or logarithmic 'l'... ")
                continue
        print("the new population is: \n" + str(newpop))
        continue

# Chi-Square
    elif action == 'chi':
        chiSq = chisq()
        print(chiSq)
        continue

    elif action == 'sdi':
        sdi = sdi()
        print("the diversity of the population is:\n" + str(sdi))
        continue
        
# Repeat If Invalid
    else: 
        print("enter valid action... ")
        continue