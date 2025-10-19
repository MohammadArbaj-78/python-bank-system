
list={'1. what is your name':'arbaj','2. why from':'manawar','3. what is your age':'21','4. what is your country':'india'}
def quiz():
    score=0
    print('Lets start game')
    for i,j in list.items():
        print(i)
        a=input('enter answer')
        if(a.lower()==j):
            print('write answer')
            score+=1
        else:
            print('wrong answer')
    
    print('your score :',score)
    


quiz()