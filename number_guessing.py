import math
import random
import time

def search(array,low,high,num,count):
    print(f"You have only {count} chances left")
    guess=int(input("Enter your guess:"))
    low=low
    high=high
    mid=math.floor((low+high)/2)
    if count==1:
        print("You exhausted all your chances....")
        print("The number was:",num)
        return None
    count-=1
    if num<guess:
        if num<mid:
            high=mid
            print("The number is too far!!")
            print("The new range to guess is between:",low,"&",high)
            search(array,low,high,num,count)
        else:
            low=mid
            print("The number is too low!!")
            print("The new range to guess is between:",low,"&",high)
            search(array,low,high,num,count)
    elif num>guess:
        if num>mid:
            low=mid
            print("The number is too low!!")
            print("The new range to guess is between:",low,"&",high)
            search(array,low,high,num,count)
        else:
            high=mid
            print("The number is too far!!")
            print("The new range to guess is between:",low,"&",high)
            search(array,low,high,num,count)
    
    else:
        print("Congratulations you guessed it right!!!!!")



lr=int(input("Enter the lower range:"))
ur=int(input("Enter upper range:"))
temp=[]
for i in range(lr,ur+1):
    temp.append(i)
print("The system is choosing a random number between the range.......")
time.sleep(3)
print("The system has choosen it's number...")
num=random.randint(lr,ur)
#print(num)
low=temp[0]
high=temp[len(temp)-1]
count=random.randint(5,10)
search(temp,low,high,num,count)