#task 9
#Taranenko Mykyta
#03,09.2023




s = 1
st = 2
currentNumber = st
for row in range(2, 6):
    for col in range(s, st):
        currentNumber -= 1
        print(currentNumber, end=' ')
    print("")
    s = st
    st += row
    currentNumber = st