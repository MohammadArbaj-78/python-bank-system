
import random              # random module for random values

print('Are you ready to rock,paper,scissors ')  

a=input()                      
if(a.lower()=='ready'):           # use of if statement for compair ready
    print('Game start')
    print('ROCK PAPER SCISSORS !')
    for i in range(5):            # for loop to iterate cod within loop 
     e=input()
     c=random.choice(['Rock','Paper','Scissors'])  # use of random function choic to random value
     if(c==e.title()):                             # in if statement compair c to e.title function means string first latter capital
      print(f'User :{e} - computer :{c}')
      print('Match drow !')
     elif(c=='Rock' and e.title()=='Scissors'):    # two condition compair by and keyword
       print(f'User :{e} - computer :{c}')
       print('computer are winner') 
     elif(c=='Paper' and e.title()=='Rock'):       # two condition compair by and keyword
       print(f'User :{e} - computer :{c}')
       print('computer are winner')
     elif(c=='Scissors' and e.title()=='Paper'):   # two condition compair by and keyword
       print(f'User :{e} - computer :{c}')
       print('computer are winner')
     elif(e.lower()=='exit'):                         # e.lower means lower value compair to exit
       print('Ok exit !')
       break                                          # breaK statement use to out of loop
     else:
       print(f'User :{e} - computer :{c}')
       print('Congretulation User are winner !')
else:
    print('Ok exit !')                                 # print exit