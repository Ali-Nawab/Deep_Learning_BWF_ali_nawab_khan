
while True:
    try:
        a = int(input("Enter a number: "))
        b = int(input("Enter another number: "))
        print(a+b)
    except ValueError:
        print("You can't add these two together.")
        
