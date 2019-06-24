alpha = input("Enter alphabet to search : ")

for i,ch in enumerate("INDIA"):
    if ch==alpha:
        print(alpha, " found at position", i)
        break
else:
    print(alpha, "was not found")