
# Program #1: Random Dice
# Write a "randDice" function (with no input) that randomly chooses two numbers between 1 and 6 (inclusive) and then adds them (this is to simulate the rolling of 2 dice).  
# The dice sum will be the output of this function.
#programmer: Devin Goshaw
#date:10/6/25
#program: dice average program
#programmer:Devin Goshaw 
#date: 10/7/2025
#program:Random dice program
import random
def randDice():
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    return dice1 + dice2

def main():
    total = 0
    for _ in range(100):
        total += randDice()
    
    average = total / 100
    print("Average of 100 dice rolls=", round(average, 2))

main()

#########
# Then write a mainline that calls the "randDice" function 100 times in a for loop.  
# The mainline then prints the average of the 100 rolls, rounded to the nearest 0.01.


