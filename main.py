def calculateHeight(smallChest, bigChest, wishedHeight):
    heightOfBigChest = 5
    heightOfSmallChest = 1
    
    totalHeight = (smallChest * heightOfSmallChest) + (bigChest * heightOfBigChest)
    difference = wishedHeight - totalHeight
    
    if difference >= 1:
        return difference
    elif difference == 0:
        return 0
    elif difference < 0:
        return 404
    else:
        return -1

# inputs
smallChest = int(input("Geben Sie die Anzahl kleiner Kisten an: "))
bigChest = int(input("Geben Sie die Anzahl großer Kisten an: "))
wishedHeight = int(input("Geben Sie die gewünschte Höhe an: "))

# output
answer = calculateHeight(smallChest, bigChest, wishedHeight)
if answer == -1:
    print("Die gewünschte Höhe kann nicht erreicht werden.")
elif answer == 0:
    print("Die gewünschte Höhe wird genau erreicht.")
elif answer == 404:
    print("Es wurden zu viele Kisten angegeben.")
else:
    print("Die benötigte Anzahl an Kisten beträgt: ", answer)