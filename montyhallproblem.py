pick=[1,2,3]
car=[1,2,3]
correctguesses=0
totalguesses=0
for i in pick:
    for j in car:
        if i == j: #if i==j that means your pick is at the same door as car so when you switch the door you are 
            correctguesses+=0 #guaranteed to miss the car 
            totalguesses+=1
        else:
            correctguesses+=1 #in any other scenario when show host reveals the goat and you switch, you win 100%
            totalguesses+=1
print(correctguesses/totalguesses*100,"%")
