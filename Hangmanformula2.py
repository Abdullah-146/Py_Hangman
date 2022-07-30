import random
from list import list ,stage
a= list

stages = stage

logo = ''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    '''


def basos():
 print(logo)
 b = random.randint(0, 2)

 blank = []
 for i in range(len(a[b])):
     blank += '_'
 print(blank)
 bool = True
 counterArray=[]
 negativeArray=[]
 i=0
 while(bool and i<7):
     i+= 1
     v =len(counterArray)

     r = len(stages) -len(negativeArray)
     print(stages[r-1])

     if (v  < len(a[b])):
         bool  = True


     else:
         bool=False
         print('game ended you won i lost')
         return
     guess = str(input("enter guessed letter == a--z \n")).lower()
     for index,item in  enumerate(a[b]):
       if (guess==item):
         print(item)
         blank[index] = item
         counterArray.append(item)
     if guess not in a[b]:
       negativeArray.append('g')
       print('please! dont get me killed')

     print(blank)


    # guess = str(input("enter guessed word ")).lower()





basos()
