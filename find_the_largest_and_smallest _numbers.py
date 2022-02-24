#Algorithm to find the largest and smallest numbers in the array (without using a function)

n = [int(i) for i in input("Please enter with a space: ").split()]

maxNumber = n[0]
maxNumberIndex = 0
minNumberIndex = 0
minNumber = n[0]

for i in range(0, len(n)):
    if (n[i] > maxNumber):
        maxNumberİndex = i
        maxNumber = n[i]

    elif (n[i] < minNumber):
        minNumberIndex = i
        minNumber = n[i]

print("Maximum value and index value: " + str(maxNumber) + " " +
      str(maxNumberİndex) + "\n" + "Minimum value and index value: " +
      str(minNumber) + " " + str(minNumberIndex))
