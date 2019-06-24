def message(a, *args, **pairs):
    print("value of a: ", a)
    for num in args:
        print(num, end="\t")
    print("\n\n")
    # First method to print Dictionary
    for k in pairs:
        print(k, " = ", pairs[k])
    print()

    # Second method to print the Dictionary
    mykeys = sorted(pairs.keys())
    for k in mykeys:
        print(k, ":", pairs[k])
    return

message("A", "B", "C", "D", name = "Rishabh", phone = 9998887776, city = "Lucknow")


# Rule:-
# First compulsory variable, then optional array and then optional dictionary