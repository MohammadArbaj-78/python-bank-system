
import random         # import random module take random number 

print('I am thinking random number')
print('Are you Gauss number')
print('your chance only 10')
print('Ok...')

a=random.randint(1,100)     # raindom number 1 to 100 by random function 'ramdint'
                                                   
for i in range(10):          # for loop for range 10     
  b=input('gauss  and enter number in 1 to 100 :')
  if(b.lower()=='exit'):           # using if statement and compair exit to lower input value
      # this cod exit not work with space in type on terminal
      print('Right answer :',a)
      break                       # brake statement to jamp out of loop
  elif not b.isdigit():           # in elif statement to chek isdigit() means digit value is equal no
     raise('enter value invalid please enter number 1 to 100')     # reasing costom error
     break                        # brake statement to jamp out of loop
  elif(int(b)==a):                # b convert in int and compair to a
    print('are you gauss',a)
    print('your answer is write')
    print('congretulation !!')       
    break                         # brake statement to jamp out of loop
  else:
    print('your answer is wrong') # last print else statement in loop