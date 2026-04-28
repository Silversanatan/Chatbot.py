def is_short():
    inp = input("Enter a string: ")
    length = len(inp)
    
    if length < 10:
        print("that's short!")
    elif length == 10:
        print("It's 10")
    else:
        print("That's long!")