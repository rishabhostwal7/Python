'''for num in range(1, 11):
    print(num)
    if num == 5:
        break
else:
    print("This is the else block of for loop")

while False:
    print("Inside while block")
else:
    print("This is the else block")

'''
alpha = input("Enter alphabet to search : ")

for ch in "INDIA":
    if ch==alpha:
        print(alpha, " found")
        break
else:
    print(alpha, "was not found")