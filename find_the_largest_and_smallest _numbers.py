#Algorithm to find the largest and smallest numbers in the array (without using a function)

n = [int(i) for i in input("Birer bosluk birakarak giriniz: ").split()]

bigNumber = n[0]
bigNumberIndex = 0
smallNumberIndex = 0
smallNumber = n[0]

for i in range(0, len(n)):
    if (n[i] > bigNumber):
        bigNumberİndex = i
        bigNumber = n[i]

    elif (n[i] < smallNumber):
        smallNumberIndex = i
        smallNumber = n[i]

print("En buyuk deger ve indis degeri: " + str(bigNumber) + " " +
      str(bigNumberİndex) + "\n" + "En kucuk deger ve indis degeri: " +
      str(smallNumber) + " " + str(smallNumberIndex))
