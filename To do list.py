
print('your to do list !')

list=['python','namaz','mamulat','ilm','home']

m=0
for i in list:
    m+=1
    print(m,'.',i)

for i in range(5):
  n=0
  t=input('Whats your need...')

  if(t.lower()=='add'):
    ts=input('Ok--enter your task...')
    for i in ts:
      list.append(i)
    print('your task added succesfully...')
  elif(t.lower()=='remove'):
    ts=input('Ok--enter remove task...')
    list.remove(ts)
    print('your task remove succesfully...')
  elif(t.lower()=='view'):
    for i in list:
      n+=1
      print(n,'.',i)
  else:
    print('Ok exit to do list')
    break