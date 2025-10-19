
import random

print('Are you generate  password')

a=input()
def pg():

 if(a.lower()=='yes' or a.lower()=='onemore'):
        print('Ok your password are Generated')
        c=random.choice(['ad86@F!A$D','H@g64Dr3%O','DF@f54#e!E','PG#r42$!G*','B2s5!g#h&9'])
        print('your password :',c)

pg()
for i in range(5):
    e=input('for next password type "onemore" and to out of cod type "exit"')
    if(e.lower()=='onemore'):
          pg()
    elif(e.lower()=='exit'):
          print('Ok exit')
          break