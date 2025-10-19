
import random                   # Using random module


for i in range(10):             # for loop use to new dice roll
  a=input('play dice roller .')           # take user input
  if(a.lower()=='yes'):                   # user input compair to yes
    print('Dice roll...')
    b=random.randint(1,6)                 # assign in b random value by randint function
    print('Result :',b)                   # and print dice result
  else:
    print('ok exit..')                    # in else part for exit use break statement
    break