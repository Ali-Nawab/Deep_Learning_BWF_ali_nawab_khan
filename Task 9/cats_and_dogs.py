with open("cats.txt", "w") as file_object:
    file_object.write("clowder\n")
    file_object.write("kitten\n")
    file_object.write("pussy\n")
    
with open("dogs.txt", "w") as file_object1:
    file_object1.write("puppy\n")
    file_object1.write("pooch\n")
    file_object1.write("hound\n")
    
try:
    with open("cats.txt") as file_object:
        contents = file_object.read()
        print(contents.rstrip())
        
except FileNotFoundError:
    print("File is not found in directory.")
    


print(file_object1)