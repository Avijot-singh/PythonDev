#Break statements

for i in range(12):
    if(i == 10):
        break 
    print("5 X ", i + 1, "=", 5 * (i + 1))
print("Left the loop")




#Break and Continue Statements

for i in range(12):
    if(i == 10):
        print("Skip the iteration")
        continue
    print("5 X ", i , "=", 5 * i)

i = 0
while True:
    print(i)
    i = i + 1
    if(i%100 == 0): # is i divisible by 100
        break


    