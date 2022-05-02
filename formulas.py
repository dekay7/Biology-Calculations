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
    while True:    
        if (r==None) and (N==None) and (t==None) and (K==None):
            r = Fraction(input("enter the per capita growth rate: \n"))
            N = Fraction(input("enter the initial population size: \n"))
            t = Fraction(input("enter the difference in time (dt): \n"))
            K = Fraction(input("enter the carrying capacity: \n"))
            break
        else: 
            break
    newpop = float((N * t * ((K-N)/N)) + N)
    return newpop

# Chi-Square
def chisq(observed=None, expected=None):
    if observed == None and expected == None:
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
def sdi(n=None, N=None):
    if n == None and N == None:
        n = []
        print("enter species #s: ")
        while True:
            value = input()
            if value != 's':
                n.append(Fraction(value))
                continue
            else:
                break
        N = input("enter population #: \n")
    if N == 'a':
        N = sum(n)
    numerator = []
    nreps = len(n)
    for i in range(nreps):
        numerator.append(float(n[i] * (n[i]-1)))
    numsum = sum(numerator)
    sdi = (1 - math.pow((numsum / (Fraction(N) * (Fraction(N)-1))), 2))
    return sdi

# Initialize Calculator
while True:
    action = str(input("which calculation? (popg, chi, sdi, exit)\n"))

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
        print("chi square value is: " + str(chiSq))
        continue

# Simpson's Diversity Index
    elif action == 'sdi':
        simpdi = sdi()
        print("the diversity of the population is:\n" + str(simpdi))
        continue
        
# Repeat If Invalid
    else: 
        print("enter valid action... ")
        continue
